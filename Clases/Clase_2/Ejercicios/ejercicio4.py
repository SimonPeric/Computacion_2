#Diseña un programa donde se creen dos hijos de manera secuencial: se lanza el primero, se espera a que finalice, y luego se lanza el segundo. 
#Cada hijo debe realizar una tarea mínima.

import os
import time

pid1 = os.fork()

if pid1 == 0:
    print("Soy el primer hijo.")
    time.sleep(1)
    os._exit(0)  
os.wait()

pid2 = os.fork()

if pid2 == 0:
    print("Soy el segundo hijo.")
    time.sleep(1)
    os._exit(0)  
os.wait()
