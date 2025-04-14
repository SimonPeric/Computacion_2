#Crea un programa que genere un proceso hijo utilizando fork() y que ambos (padre e hijo) impriman sus respectivos PID y PPID.
#El objetivo es observar la relación jerárquica entre ellos.

import os

pid = os.fork()

if pid > 0:
    print("Soy el proceso padre, PID:", os.getpid(), "PPID:", os.getppid())  
else:
    print("Soy el proceso hijo, PID:", os.getpid(), "PPID:", os.getppid())  
