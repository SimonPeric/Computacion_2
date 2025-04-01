#Haz que un proceso hijo reemplace su contexto de ejecución con un programa del sistema, por ejemplo, el comando ls -l, utilizando exec().

import os

pid = os.fork()

if pid == 0:
    os.execlp ("ls","lp","-l")
else:
    os.wait