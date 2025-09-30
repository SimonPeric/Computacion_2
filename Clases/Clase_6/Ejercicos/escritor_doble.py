import os

fifo_path = "fifo_cursor"

if not os.path.exists(fifo_path):
    os.mkfifo(fifo_path)

# Primer envío
print("[Escritor] Enviando primera tanda...")
with open(fifo_path, "w") as fifo:
    fifo.write("Linea A\nLinea B\n")

# Segundo envío
print("[Escritor] Enviando segunda tanda...")
with open(fifo_path, "w") as fifo:
    fifo.write("Linea A\nLinea B\n")

print("[Escritor] Listo.")
