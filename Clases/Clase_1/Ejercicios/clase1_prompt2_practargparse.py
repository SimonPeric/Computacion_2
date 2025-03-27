import os
import argparse

def main():
    parser = argparse.ArgumentParser(description="Un programa que maneja argumentos")

    parser.add_argument("-i", "--input", type=str, nargs='+', required=True, help="Lista de archivos de entrada")
    parser.add_argument("-o", "--output", required=True, help="Archivo de salida")
    parser.add_argument("-r", "--repeticiones", type=int, default=1, help="Número de veces que se debe repetir la operación")

    args = parser.parse_args()
    
    for file in args.input:
        if os.path.exists(file):
            with open(file, "r") as archivo_entrada:
                num_lineas_ent = sum(1 for linea in archivo_entrada)

            for _ in range(args.repeticiones):
                with open(args.output, "a") as archivo_salida:
                    archivo_salida.write(f"El número de líneas del archivo {file} es: {num_lineas_ent}\n")
            
                print(f"El número de líneas del archivo {file} es: {num_lineas_ent}")
        else:
            print(f"ERROR: El archivo de entrada '{file}' no existe")

if __name__ == "__main__":
    main()

