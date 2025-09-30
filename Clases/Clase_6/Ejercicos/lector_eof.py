import os

fifo_path = "fifo_eof"

if not os.path.exists(fifo_path):
    os.mkfifo(fifo_path)

print("[Lector] Esperando datos...")
with open(fifo_path, "r") as fifo:
    for linea in fifo:
        print(f"[Lector] Recibido: {linea.strip()}")
    print("[Lector] Fin de datos (EOF recibido).")
