#Objetivo: comprobar la creación de procesos y la correcta espera del padre.

#Enunciado: escribe un programa que cree dos procesos hijo mediante multiprocessing.Process, cada uno imprimiendo su propio pid.
#El proceso padre debe esperar a que ambos terminen y luego imprimir un mensaje de cierre.

from multiprocessing import Process
import os

def hijo():
    print (f"Soy el proceso hijo, PID {os.getpid()}")

if __name__ == "__main__":
    procesos = [Process(target = hijo) for i in range(2)]

    for i in procesos:
        i.start()
    
    for i in procesos:
        i.join()

    print(f"Soy el proceso padre, PID {os.getpid()}")
