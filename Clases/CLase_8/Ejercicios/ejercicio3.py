#Objetivo: demostrar una condición de carrera y su corrección con Lock.

#Enunciado: crea un contador global al que dos procesos suman 1, cincuenta mil veces cada uno. 
#Realiza primero la versión sin Lock (para evidenciar valores erróneos) y luego protégela con un Lock, mostrando el resultado correcto (100 000).

from multiprocessing import Process, Value, Lock

#Sin Lock

def contador(n, total):
    for c in range(n):
        total.value += 1   

if __name__ == "__main__":
    n = 50000
    total = Value('i', 0)  

    procesos = [Process(target=contador, args=(n, total)) for i in range(2)]

    for p in procesos:
        p.start()
    for p in procesos:
        p.join()

    print(f"Contador total {total.value}")

#Con Lock

def contador(n, total, lock):
    for c in range(n):
        with lock:
            total.value += 1   

if __name__ == "__main__":
    n = 50000
    total = Value('i', 0)
    lock = Lock()  

    procesos = [Process(target=contador, args=(n, total, lock)) for i in range(2)]

    for p in procesos:
        p.start()
    for p in procesos:
        p.join()

    print(f"Contador total {total.value}")

