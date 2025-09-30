import os
import time

fifo_path = "fifo_eof"

if not os.path.exists(fifo_path):
    os.mkfifo(fifo_path)

print("[Escritor] Enviando datos...")
with open(fifo_path, "w") as fifo:
    fifo.write("Mensaje 1\n")
    fifo.write("Mensaje 2\n")
    time.sleep(1)

print("[Escritor] Cerrando FIFO.")
