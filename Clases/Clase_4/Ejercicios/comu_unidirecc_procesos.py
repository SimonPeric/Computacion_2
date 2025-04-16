import os

read_fd, write_fd = os.pipe()

pid = os.fork()

if pid > 0:
    # Proceso Padre
    os.close(read_fd)
    numero = "5"
    os.write(write_fd, numero.encode())
    os.close(write_fd)
    os.waitpid(pid, 0)

else:
    # Proceso Hijo
    os.close(write_fd)
    data = os.read(read_fd, 1024)
    numero = int(data.decode())
    resultado = numero * 2
    print(f"El numero recibido es: {numero}")
    print(f"El resultado es: {resultado}")
    os.close(read_fd) 