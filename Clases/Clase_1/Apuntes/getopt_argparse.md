# Resumen Teórico: Manejo de Argumentos en Python con getopt y argparse

## 1️⃣ Conceptos Básicos

### ¿Qué son los argumentos de línea de comandos?
Son valores que se pasan a un script de Python cuando se ejecuta desde la terminal. Permiten modificar el comportamiento del programa sin cambiar el código.

### ¿Por qué son importantes?
✅ Permiten automatizar tareas.
✅ Facilitan la reutilización del código.
✅ Hacen los programas más flexibles.

### Ejemplo de ejecución de un script en la terminal:
```bash
python3 mi_script.py argumento1 argumento2
```

---

## 2️⃣ Uso de getopt

`getopt` permite manejar argumentos de línea de comandos de manera simple.

### Importar y usar getopt:
```python
import sys
import getopt

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "n:e:", ["nombre=", "edad="])
    except getopt.GetoptError as err:
        print("Error:", err)
        sys.exit(1)
    
    nombre = ""
    edad = None
    
    for opcion, valor in opts:
        if opcion in ("-n", "--nombre"):
            nombre = valor
        elif opcion in ("-e", "--edad"):
            edad = int(valor)
    
    print(f"Nombre: {nombre}, Edad: {edad}")

if __name__ == "__main__":
    main()
```

### Ejemplo de ejecución:
```bash
python3 script.py -n Juan -e 25
```
🔹 `getopt` es útil para argumentos simples pero carece de validaciones avanzadas.

---

## 3️⃣ Uso de argparse

`argparse` es más potente y fácil de usar que `getopt`. Permite definir argumentos obligatorios, opcionales y manejar distintos tipos de datos.

### Importar y definir argumentos con argparse:
```python
import argparse

def main():
    parser = argparse.ArgumentParser(description="Ejemplo de argparse")
    
    parser.add_argument("-i", "--input", required=True, help="Archivo de entrada")
    parser.add_argument("-o", "--output", required=False, default="salida.txt", help="Archivo de salida")
    parser.add_argument("-r", "--repeticiones", type=int, default=1, help="Número de repeticiones")
    parser.add_argument("-v", "--verbose", action="store_true", help="Modo detallado")
    
    args = parser.parse_args()
    
    print(f"Archivo de entrada: {args.input}")
    print(f"Archivo de salida: {args.output}")
    print(f"Repeticiones: {args.repeticiones}")
    if args.verbose:
        print("Modo detallado activado")

if __name__ == "__main__":
    main()
```

### Ejemplo de ejecución:
```bash
python3 script.py -i datos.txt -o resultado.txt -r 3 -v
```
📌 `argparse` maneja la conversión automática de tipos y genera mensajes de ayuda.

---

## 4️⃣ Escritura y lectura de archivos

### Leer un archivo línea por línea:
```python
with open("archivo.txt", "r") as archivo:
    lineas = archivo.readlines()
    print(f"El archivo tiene {len(lineas)} líneas")
```

### Escribir en un archivo:
```python
with open("salida.txt", "w") as archivo:
    archivo.write("Hola, este es un archivo de salida\n")
```

### Escribir sin sobrescribir el contenido previo (modo append `a`):
```python
with open("salida.txt", "a") as archivo:
    archivo.write("Otra línea de texto\n")
```

---

## 5️⃣ Validaciones comunes en scripts
✅ Verificar si un archivo existe:
```python
import os
if os.path.exists("archivo.txt"):
    print("El archivo existe")
else:
    print("ERROR: El archivo no existe")
```

✅ Evitar errores con `try-except`:
```python
try:
    with open("archivo.txt", "r") as archivo:
        contenido = archivo.read()
except FileNotFoundError:
    print("Error: No se encontró el archivo")
```

---

## 6️⃣ Ejemplos de ejecución y pruebas

### Comprobar si un argumento es obligatorio:
```bash
python3 script.py -i entrada.txt  # Mostrará un error si falta el argumento obligatorio
```

### Verificar cómo argparse genera ayuda automáticamente:
```bash
python3 script.py --help
```
🔹 Mostrará una descripción detallada de los argumentos disponibles.

### Ejecutar con distintos parámetros:
```bash
python3 script.py -i entrada.txt -o salida.txt -r 3 -v
```
🔹 Mostrará detalles en pantalla y escribirá en el archivo de salida.

---

## 📌 Resumen final
✅ `getopt` es útil para casos simples, pero `argparse` es más flexible.
✅ `argparse` permite manejar valores predeterminados, tipos de datos y generación automática de ayuda.
✅ Aprendimos a leer y escribir archivos desde scripts de Python.
✅ Validamos la existencia de archivos y manejamos errores adecuadamente.

📚 Para más práctica, revisá:
🔹 [Documentación oficial de argparse](https://docs.python.org/3/library/argparse.html)
🔹 [Ejercicios extra en Python](https://www.practicepython.org/)

