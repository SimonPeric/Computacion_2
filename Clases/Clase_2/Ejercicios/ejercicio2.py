#Escribe un programa donde un proceso padre cree dos hijos diferentes (no en cascada), y cada hijo imprima su identificador.
#El padre deberá esperar a que ambos terminen.

import os

for i in range(2):
    pid =os.fork()
    if pid == 0:
        print("Soy el proceso hijo:",[i], "mi PID es:", os.getpid())
        os._exit(0)

for _ in range (2):
    os.wait()
