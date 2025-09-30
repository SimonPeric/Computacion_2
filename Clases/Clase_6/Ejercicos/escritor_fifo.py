import os
import time

fifo_path = "mi_fifo_cursor"

if not os.path.exists(fifo_path):
    os.mkfifo(fifo_path)

print("[Escritor] Esperando para escribir...")
time.sleep(2)

with open(fifo_path, "w") as fifo:
    fifo.write("Linea 1\nLinea 2\nLinea 3\n")
    print("[Escritor] Mensaje enviado.")
