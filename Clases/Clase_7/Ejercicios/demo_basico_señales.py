# demo_basico_senales.py
import signal
import sys
import os
import time

contador = 0
archivo_estado = "estado.txt"

def on_sigint(signum, frame):
    print(f"\n[handler] Recibido SIGINT ({signum}). Limpiando y saliendo con código 130...")
    sys.exit(130)

def on_sigterm(signum, frame):
    print(f"\n[handler] Recibido SIGTERM ({signum}). Guardando estado...")
    time.sleep(0.5)
    sys.exit(0)

def handle_sighup(signum, frame):
    print("SIGHUP recibido: recargando configuración... (simulada)")

def handle_sigterm(signum, frame):
    global contador
    print("SIGTERM recibido. Guardando estado en archivo...")
    with open(archivo_estado, "w") as f:
        f.write(f"Contador final: {contador}\n")
    print("Estado guardado. Saliendo.")
    exit(0)

signal.signal(signal.SIGINT, on_sigint)
signal.signal(signal.SIGTERM, on_sigterm)
signal.signal(signal.SIGHUP, handle_sighup)
signal.signal(signal.SIGTERM, handle_sigterm)

print("PID:", os.getpid() if 'os' in globals() else __import__('os').getpid())
print("Corre y espera señales (Ctrl+C para SIGINT)...")
print("Envia SIGHUP con: kill -HUP <PID>")
print("Enviar SIGTERM con: kill -TERM <PID>")
while True:
    contador += 1
    print(f"Contador: {contador}")
    time.sleep(2)
