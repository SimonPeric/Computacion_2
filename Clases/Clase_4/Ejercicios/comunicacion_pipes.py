import os

# Crear el pipe
read_fd, write_fd = os.pipe()

# Crear un proceso hijo
pid = os.fork()

if pid == 0:
    # --- PROCESO HIJO ---
    os.close(write_fd)  # Cerramos el extremo de escritura (solo lee)
    
    # Leer datos
    data = os.read(read_fd, 1024)
    print(f"Hijo recibió: {data.decode()}") #.decode() convierte bytes a string
    os.close(read_fd)

else:
    # --- PROCESO PADRE ---
    os.close(read_fd)  # Cerramos el extremo de lectura (solo escribe)
    
    # Escribir datos
    mensaje = "Hola desde el padre"
    os.write(write_fd, mensaje.encode()) #.encode() convierte string a bytes
    os.close(write_fd)
