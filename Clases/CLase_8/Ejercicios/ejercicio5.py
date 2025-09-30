#Objetivo: diseñar un pipeline productor–consumidor usando Pipe doble.

#Enunciado: crea dos procesos hijos: productor genera 10 números pseudo‑aleatorios y los envía al padre; 
# el padre los reenvía a un consumidor, que imprime el cuadrado de cada número. Implementa el pipeline con dos Pipe(), 
# asegurando el cierre limpio de extremos y detectando fin de datos mediante envío del valor None.

from multiprocessing import Process, Pipe
import random

def productor(conn):
    for _ in range(10):  
        num = random.randint(0, 20)
        conn.send(num)
    conn.send(None)  
    conn.close()

def consumidor(conn):
    while True:
        msg = conn.recv()
        if msg is None:  
            break
        print(f"Número recibido: {msg}, al cuadrado: {msg**2}")
    conn.close()

if __name__ == "__main__":
    padre_conn1, hijo_conn1 = Pipe()
    padre_conn2, hijo_conn2 = Pipe()

    p1 = Process(target=productor, args=(hijo_conn1,))
    p2 = Process(target=consumidor, args=(hijo_conn2,))

    p1.start()
    p2.start()

    while True:
        dato = padre_conn1.recv()
        padre_conn2.send(dato)
        if dato is None:
            break

    padre_conn1.close()
    padre_conn2.close()

    p1.join()
    p2.join()
