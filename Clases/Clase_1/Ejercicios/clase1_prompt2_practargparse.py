import os
import argparse

def main():
    parser = argparse.ArgumentParser(description="Un programa que maneja argumentos")

    parser.add_argument("-i", "--input", required=True, help="Archivo de entrada")
    parser.add_argument("-o", "--output", required=True, help="Archivo de salida")
    parser.add_argument("-r", "--repeticiones", type=int, default=1, help="Número de veces que se debe repetir la operación")
    parser.add_argument("-v", "--verbose", action="store_true", help="Activa el modo detallado")
    parser.add_argument("-p", "--palabras", type=str, nargs='+', help="Lista de palabras a mostrar")

    args = parser.parse_args()

    if os.path.exists(args.input):
        with open(args.input, "r") as archivo_entrada:
            num_lineas_ent = sum(1 for linea in archivo_entrada)

        for _ in range(args.repeticiones):
            with open(args.output, "a") as archivo_salida:
                archivo_salida.write(f"El número de líneas del archivo de entrada es: {num_lineas_ent}\n")

            print(f"El número de líneas del archivo de entrada es: {num_lineas_ent}")

            if args.verbose:
                print("Modo detallado activado")
    else:
        print(f"ERROR: El archivo de entrada '{args.input}' no existe")

    if args.palabras:
        print("\nPalabras ingresadas:")
        for palabra in args.palabras:
            print(palabra)

if __name__ == "__main__":
    main()
