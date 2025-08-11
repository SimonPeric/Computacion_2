import json
import hashlib
import os

BLOCKCHAIN_FILE = "blockchain.json"
REPORTE_FILE = "reporte.txt"

def calcular_hash(prev_hash, datos, timestamp):
    s = prev_hash + json.dumps(datos, sort_keys=True) + timestamp
    return hashlib.sha256(s.encode()).hexdigest()

def main():
    if not os.path.exists(BLOCKCHAIN_FILE):
        print("No se encontró", BLOCKCHAIN_FILE)
        return

    with open(BLOCKCHAIN_FILE, "r") as f:
        try:
            chain = json.load(f)
        except Exception as e:
            print("Error leyendo blockchain.json:", e)
            return

    corruptos = []
    prev_hash = "0" * 64
    total_bloques = len(chain)
    alertas = 0

    sum_frec = 0.0
    sum_pres = 0.0
    sum_oxi = 0.0

    for idx, block in enumerate(chain):
        expected_prev = block.get("prev_hash", "")
        if expected_prev != prev_hash:
            corruptos.append((idx, "prev_hash no coincide"))
        
        datos = block.get("datos")
        ts = block.get("timestamp", "")
        recal = calcular_hash(prev_hash, datos, ts)
        if recal != block.get("hash"):
            corruptos.append((idx, "hash incorrecto"))
        
        if block.get("alerta"):
            alertas += 1
        
        try:
            sum_frec += float(datos["frecuencia"]["media"])
            sum_pres += float(datos["presion"]["media"])
            sum_oxi += float(datos["oxigeno"]["media"])
        except Exception:
            pass

        prev_hash = block.get("hash", prev_hash)

    
    avg_frec = sum_frec / total_bloques if total_bloques else 0.0
    avg_pres = sum_pres / total_bloques if total_bloques else 0.0
    avg_oxi = sum_oxi / total_bloques if total_bloques else 0.0

    # escribir reporte
    with open(REPORTE_FILE, "w") as rf:
        rf.write(f"Reporte de verificación - {BLOCKCHAIN_FILE}\n")
        rf.write(f"Total de bloques: {total_bloques}\n")
        rf.write(f"Bloques con alerta: {alertas}\n")
        rf.write("\nPromedios (sobre medias de cada bloque):\n")
        rf.write(f"- Frecuencia promedio: {avg_frec:.2f}\n")
        rf.write(f"- Presión sistólica promedio: {avg_pres:.2f}\n")
        rf.write(f"- Oxígeno promedio: {avg_oxi:.2f}\n")
        rf.write("\nBloques corruptos / inconsistencias detectadas:\n")
        if not corruptos:
            rf.write("Ninguno. Cadena válida.\n")
        else:
            for idx, motivo in corruptos:
                rf.write(f"- Bloque {idx}: {motivo}\n")

    # resumen por pantalla
    print("Verificación completada.")
    print(f"Total bloques: {total_bloques}, alertas: {alertas}")
    if corruptos:
        print("Se detectaron inconsistencias. Revisa reporte.txt")
    else:
        print("Cadena íntegra.")
    print("Reporte escrito en", REPORTE_FILE)

if __name__ == "__main__":
    main()
