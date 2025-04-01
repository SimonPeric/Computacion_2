#Crea un programa que genere un proceso hijo que termine inmediatamente, pero el padre no debe recoger su estado de salida durante algunos segundos.
#Observa su estado como zombi con herramientas del sistema.

import os
import time

pid = os.fork()

if pid > 0:
    print("Soy el proceso padre, estoy esperando 2 seg para ver a mi hijo transformarse en zombie")
    time.sleep(2)
    print("Finaliza sin llamar a wait()")
    os._exit(0)
else:
    print("Soy el proceso hijo, y termino inmediatamente")
    os._exit(0)