import os
from multiprocessing import Process

def tarea(numero):
    print(f"Proceso {numero} ejecutándose, PID={os.getpid()}")

if __name__ == "__main__":
    procesos = []
    
    # Crear 4 procesos
    for i in range(4):
        p = Process(target=tarea, args=(i,))
        procesos.append(p)
        p.start()
    
    # Esperar a que todos terminen
    for p in procesos:
        p.join()
    
    print("Todos los procesos han terminado")
