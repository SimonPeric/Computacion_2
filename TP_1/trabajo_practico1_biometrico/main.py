import multiprocessing
import random
import time
from datetime import datetime
import numpy as np
import json
import hashlib
import os
import signal
import sys

SAMPLES = 60  
BLOCKCHAIN_FILE = "blockchain.json"

def generar_muestra():
    return {
        "timestamp": datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
        "frecuencia": random.randint(60, 180),
        "presion": [random.randint(110, 180), random.randint(70, 110)],
        "oxigeno": random.randint(90, 100)
    }

def analizador(nombre, campo, conn, q_result, stop_event): # Recibe muestras por conn (Pipe). Mantiene ventana móvil de 30 valores y cada vez que llega una muestra envía al verificador un dict con tipo,timestamp,media,desv. Cuando recibe "FIN" cierra y envía un sentinel "FIN" a la cola de resultados.
    ventana = []
    try:
        while True:
            try:
                datos = conn.recv()
            except EOFError:
                break

            if datos == "FIN": # señal de terminación: avisar al verificador que este analizador terminó
                q_result.put("FIN")
                break 
            
            if campo == "presion": # extraer valor según el campo
                valor = datos["presion"][0]  # sistólica
            else:
                valor = datos[campo]

            ventana.append(valor)
            if len(ventana) > 30:
                ventana.pop(0)

            media = float(np.mean(ventana))
            desv = float(np.std(ventana, ddof=0))  # población

            resultado = {
                "tipo": campo,
                "timestamp": datos["timestamp"],
                "media": media,
                "desv": desv
            }
            q_result.put(resultado)

            if stop_event.is_set(): # permitir terminar de forma limpia si proceso el padre lo solicita
                q_result.put("FIN")
                break
    finally:
        try:
            conn.close()
        except Exception:
            pass

def calcular_hash(prev_hash, datos, timestamp):
    s = prev_hash + json.dumps(datos, sort_keys=True) + timestamp
    return hashlib.sha256(s.encode()).hexdigest()

def verificador(q_result, stop_event, blockchain_file=BLOCKCHAIN_FILE):   # Lee todos los resultados desde una única cola q_result. Agrupa por timestamp hasta tener los 3 tipos y construye el bloque. Persiste blockchain.json **después de añadir cada bloque**. Finaliza cuando recibe 3 sentinels "FIN" (uno por cada analizador) y no quedan bloques pendientes.
    blockchain = [] # cargar blockchain existente si hay 
    prev_hash = "0" * 64
    if os.path.exists(blockchain_file):
        try:
            with open(blockchain_file, "r") as f:
                blockchain = json.load(f)
            if blockchain:
                prev_hash = blockchain[-1]["hash"]
        except Exception:
            print("Aviso: no se pudo cargar blockchain.json; iniciando nueva cadena.")

    pending = {}  # pending[timestamp] = { tipo: {media,desv}, ... }
    fin_count = 0
    required_types = {"frecuencia", "presion", "oxigeno"}

    while True:
        try:
            item = q_result.get(timeout=1.0)
        except Exception:
            if fin_count >= 3 and not pending: # timeout: verificar condición de salida
                break
            if stop_event.is_set():
                break
            continue

        if item == "FIN":
            fin_count += 1 # si llegaron todos los FIN y no hay pendientes, salimos
            if fin_count >= 3 and not pending:
                break
            continue

        ts = item["timestamp"] # item es un resultado
        tipo = item["tipo"]
        pending.setdefault(ts, {})[tipo] = {"media": item["media"], "desv": item["desv"]}

        if set(pending[ts].keys()) >= required_types: # tenemos las 3 señales para este timestamp: construir bloque
            frec = pending[ts]["frecuencia"]
            pres = pending[ts]["presion"]
            oxi = pending[ts]["oxigeno"]

            alerta = False  # comprobaciones: según enunciado
            mensajes_alerta = []

            if frec["media"] >= 200: # condiciones solicitadas (usar medias)
                alerta = True
                mensajes_alerta.append(f"Frecuencia fuera de rango ({frec['media']:.1f})")
            if not (90 <= oxi["media"] <= 100):
                alerta = True
                mensajes_alerta.append(f"Oxígeno fuera de rango ({oxi['media']:.1f})")
            if pres["media"] >= 200:
                alerta = True
                mensajes_alerta.append(f"Presión sistólica fuera de rango ({pres['media']:.1f})")

            datos_bloque = {
                "frecuencia": {"media": frec["media"], "desv": frec["desv"]},
                "presion": {"media": pres["media"], "desv": pres["desv"]},
                "oxigeno": {"media": oxi["media"], "desv": oxi["desv"]}
            }

            bloque = {
                "timestamp": ts,
                "datos": datos_bloque,
                "alerta": alerta,
                "prev_hash": prev_hash,
                "hash": None
            }

            bloque["hash"] = calcular_hash(prev_hash, datos_bloque, ts)
            blockchain.append(bloque)
            prev_hash = bloque["hash"]

            idx = len(blockchain) - 1
            print(f"Bloque {idx} generado. Hash: {bloque['hash']}. Alerta: {alerta}")
            if alerta:
                print("    Detalles:", "; ".join(mensajes_alerta))

            try: # persistir al disco inmediatamente
                with open(blockchain_file, "w") as f:
                    json.dump(blockchain, f, indent=2)
            except Exception as e:
                print("Error guardando blockchain:", e)

            del pending[ts]

    try:
        with open(blockchain_file, "w") as f:
            json.dump(blockchain, f, indent=2)
    except Exception:
        pass

if __name__ == "__main__":
    # CTRL+C limpio
    def sigint_handler(sig, frame):
        print("\nInterrupción recibida. Solicitando parada limpia...")
        # No podemos forzar demasiado: usar stop_event
        stop_event.set()

    signal.signal(signal.SIGINT, sigint_handler)

    # Pipes (uno por analizador)
    p_frec_princ, p_frec_anal = multiprocessing.Pipe()
    p_pres_princ, p_pres_anal = multiprocessing.Pipe()
    p_oxi_princ, p_oxi_anal = multiprocessing.Pipe()

    # Cola única para resultados (analizadores -> verificador)
    q_result = multiprocessing.Queue()

    # evento para señalizar parada (opcional)
    stop_event = multiprocessing.Event()

    proc_frec = multiprocessing.Process(
        target=analizador, args=("Proc A", "frecuencia", p_frec_anal, q_result, stop_event), daemon=False
    )
    proc_pres = multiprocessing.Process(
        target=analizador, args=("Proc B", "presion", p_pres_anal, q_result, stop_event), daemon=False
    )
    proc_oxi = multiprocessing.Process(
        target=analizador, args=("Proc C", "oxigeno", p_oxi_anal, q_result, stop_event), daemon=False
    )

    proc_verif = multiprocessing.Process(
        target=verificador, args=(q_result, stop_event, BLOCKCHAIN_FILE), daemon=False
    )

    # arrancar procesos
    proc_frec.start()
    proc_pres.start()
    proc_oxi.start()
    proc_verif.start()

    try:
        for _ in range(SAMPLES):
            muestra = generar_muestra()
            print("Principal generó:", muestra)
            # enviar a analizadores
            p_frec_princ.send(muestra)
            p_pres_princ.send(muestra)
            p_oxi_princ.send(muestra)
            time.sleep(1)

        # indicar fin a analizadores
        p_frec_princ.send("FIN")
        p_pres_princ.send("FIN")
        p_oxi_princ.send("FIN")

        # cerrar extremos parent de pipes
        try:
            p_frec_princ.close()
            p_pres_princ.close()
            p_oxi_princ.close()
        except Exception:
            pass

        # esperar a que analizadores terminen y envíen sus "FIN" a la cola
        proc_frec.join(timeout=10)
        proc_pres.join(timeout=10)
        proc_oxi.join(timeout=10)

        # esperar verificador termine (recibirá 3 "FIN" desde los analizadores)
        proc_verif.join(timeout=30)
        if proc_verif.is_alive():
            # si por alguna razón quedó vivo, pedir parada y esperar un poco
            stop_event.set()
            proc_verif.join(timeout=5)

    except KeyboardInterrupt:
        stop_event.set()
    finally:
        # asegurarse de limpiar procesos (join/terminate solo si siguen ahí)
        for p in (proc_frec, proc_pres, proc_oxi, proc_verif):
            if p.is_alive():
                p.terminate()
            p.join(timeout=1)

        # vaciar cola (si queda algo)
        try:
            while not q_result.empty():
                q_result.get_nowait()
        except Exception:
            pass

    print("Programa principal finalizado.")
