import os

fifo_path = "fifo_no_bloqueante"

if not os.path.exists(fifo_path):
    os.mkfifo(fifo_path)

# Abrir en modo lectura NO bloqueante
fd = os.open(fifo_path, os.O_RDONLY | os.O_NONBLOCK)

try:
    datos = os.read(fd, 1024)  # leer hasta 1024 bytes
    if datos:
        print(f"[Lector] Datos recibidos: {datos.decode().strip()}")
    else:
        print("[Lector] No hay datos disponibles ahora.")
finally:
    os.close(fd)
