#Imita el comportamiento de un servidor concurrente que atiende múltiples clientes creando un proceso hijo por cada uno. 
#Cada proceso debe simular la atención a un cliente con un sleep().

import os
import time

def antender_clientes(n):
    pid = os.fork()
    if pid == 0:
        print(f"[Hijo {n}] Atendiendo Cliente")
        time.sleep(3)
        print(f"[Hijo {n}] Cliente atendido")
        os._exit(0)

for cliente in range(5):
    antender_clientes(cliente)

for _ in range(5):
    os.wait()
    