import os

# Crear dos pipes: uno para cada dirección
# pipe1: padre escribe, hijo lee
# pipe2: hijo escribe, padre lee
pipe1_read, pipe1_write = os.pipe()
pipe2_read, pipe2_write = os.pipe()

pid = os.fork()

if pid == 0:
    # === PROCESO HIJO ===

    # Cerramos extremos que no usamos
    os.close(pipe1_write)  # Hijo no escribe en pipe1
    os.close(pipe2_read)   # Hijo no lee de pipe2

    # Leer número del padre
    data = os.read(pipe1_read, 1024)
    numero = int(data.decode())
    print(f"[Hijo] Recibido del padre: {numero}")

    # Procesar
    resultado = numero * 2

    # Enviar resultado al padre
    os.write(pipe2_write, str(resultado).encode())

    # Cerrar extremos usados
    os.close(pipe1_read)
    os.close(pipe2_write)

else:
    # === PROCESO PADRE ===

    # Cerramos extremos que no usamos
    os.close(pipe1_read)   # Padre no lee de pipe1
    os.close(pipe2_write)  # Padre no escribe en pipe2

    # Enviar número al hijo
    numero = "8"
    os.write(pipe1_write, numero.encode())
    os.close(pipe1_write)

    # Leer respuesta del hijo
    respuesta = os.read(pipe2_read, 1024)
    print(f"[Padre] Resultado recibido del hijo: {respuesta.decode()}")

    os.close(pipe2_read)
    os.waitpid(pid, 0)
