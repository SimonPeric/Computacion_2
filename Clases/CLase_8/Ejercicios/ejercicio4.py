#Objetivo: medir el impacto del GIL versus multiprocessing en tareas CPU‑bound.

#Enunciado: implementa la función fibonacci(n) de forma recursiva e imprímela para n = 35. Mide primero el tiempo 
#usando hilos (threading.Thread) con 4 hilos y luego con 4 procesos (multiprocessing.Process). Compara y explica la diferencia.

import time
from threading import Thread
from multiprocessing import Process

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def worker():
    fibonacci(35)

if __name__ == "__main__":
    
    #Con hilos 

    start = time.time()
    threads = [Thread(target=worker) for _ in range(4)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    end = time.time()
    print(f"Tiempo con hilos: {end - start:.4f} segundos")

    #Con procesos 

    start = time.time()
    procesos = [Process(target=worker) for _ in range(4)]
    for p in procesos:
        p.start()
    for p in procesos:
        p.join()
    end = time.time()
    print(f"Tiempo con procesos: {end - start:.4f} segundos")

# A modo de comparacion vemos que con hilos se demora mas del doble en realizar la tarea a comparacion que con procesos, ya que con procesos se utilizan 
#todos los nucleos que tengamos disponibles(4 en este caso) en cambio con hilos solo se utiliza 1.




    
