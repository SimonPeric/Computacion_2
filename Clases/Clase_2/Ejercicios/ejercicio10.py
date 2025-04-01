#Simula un escenario donde un proceso huérfano ejecuta un comando externo sin control del padre.
#Analiza qué implicaciones tendría esto en términos de seguridad o evasión de auditorías.

import os
import time

pid = os.fork()

if pid > 0:
    os._exit
else:
    print("Proceso huerfano, ejecutando:")
    os.system("ls -l /home")  #Esto es peligroso de ejecutar por que se ejecuta cualquier script de la direccion sin ninguna validacion
    time.sleep(4)             #una opcion mas segura es os.system("echo 'Soy un proceso huérfano ejecutando un comando externo'")

