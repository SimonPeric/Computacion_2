import os

fifo_path = "mi_fifo_cursor"

if not os.path.exists(fifo_path):
    os.mkfifo(fifo_path)

print("[Lector2] Esperando datos...")
with open(fifo_path, "r") as fifo:
    for linea in fifo:
        print(f"[Lector2] Leyó: {linea.strip()}")
