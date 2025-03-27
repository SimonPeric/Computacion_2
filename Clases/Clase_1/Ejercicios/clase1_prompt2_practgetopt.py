import sys
import getopt

def main():
    nombre = ""
    edad = None
    ciudad = ""

    opciones, argumentos = getopt.getopt(sys.argv[1:], "n:e:c:", ["nombre=", "edad=", "ciudad="])

    for opcion, valor in opciones:
        if opcion in ("-n", "--nombre"):
            nombre = valor
        elif opcion in ("-e", "--edad"):
            edad = int(valor)
        elif opcion in ("-c", "--ciudad"):
            ciudad = valor

    if not nombre:
        print("ERROR: Debes proporcionar un nombre con -n o --nombre.")
        sys.exit(1)  # Salir del programa con código de error

    if edad:
        print(f"Hola {nombre}, tienes {edad} años.")
    else:
        print(f"Hola {nombre}, no proporcionaste tu edad.")

    if not ciudad:
        print("ERROR: Debes proporcionar una ciudad con -c o --ciudad.")
        sys.exit(1)  # Salir del programa con código de error
    else:
        print(f"Tu ciudad es {ciudad}.")

if __name__ == "__main__":
    main()

