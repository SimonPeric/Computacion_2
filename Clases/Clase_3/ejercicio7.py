#Construye un programa que cree tres hijos en paralelo (no secuenciales). Cada hijo ejecutará una tarea breve y luego finalizará.
#El padre debe esperar por todos ellos.

import os

for _ in range(3):
    pid = os.fork()
    if pid == 0:
        print("Soy el hijo")
        os._exit(0)

for _ in range(3):
    os.wait()