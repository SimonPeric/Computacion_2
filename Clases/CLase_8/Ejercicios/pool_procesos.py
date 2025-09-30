from multiprocessing import Pool
import os

def cuadrado(n):
    print(f"Proceso {os.getpid()} calculando {n}^2")
    return n * n

if __name__ == "__main__":
    numeros = [1, 2, 3, 4, 5, 6, 7, 8]

    with Pool(processes=4) as pool:  # Pool de 4 procesos
        resultados = pool.map(cuadrado, numeros)

    print("Resultados:", resultados)
