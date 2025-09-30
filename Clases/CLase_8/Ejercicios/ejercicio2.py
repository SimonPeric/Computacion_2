#Objetivo: usar Queue para reunir resultados de varios procesos.

#Enunciado: implementa un script que genere n = 4 procesos; cada proceso calcula la suma de los primeros k = 1 , 000 , 000 enteros y 
#deposita el resultado en una Queue. El padre recoge los cuatro resultados y verifica que sean idénticos.

from multiprocessing import Process, Queue

def worker(k, q):
    q.put(sum(range(k)))

if __name__ == '__main__':
    k = 1_000_000
    q = Queue()
    ps = [Process(target=worker, args=(k, q)) for _ in range(4)]
    for p in ps: p.start()
    resultados = [q.get() for _ in ps]
    for p in ps: p.join()
    assert len(set(resultados)) == 1
    print('Todos iguales:', resultados[0])