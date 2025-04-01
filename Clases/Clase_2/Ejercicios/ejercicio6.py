#Genera un proceso hijo que siga ejecutándose luego de que el padre haya terminado. Verifica que su nuevo PPID corresponda al proceso init o systemd.

import os
import time

pid = os.fork()

if pid > 0:
    print("Soy el proceso padre y termino inmediatamente")
    os._exit(0)
else:
    print("Soy el proceso hijo y quede huerfano, mi PPID es:", os.getppid())
    time.sleep(10)