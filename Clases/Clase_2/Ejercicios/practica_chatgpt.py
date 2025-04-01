import os
import time

pid = os.fork()

if pid > 0:
    print(f"Padre ({os.getpid()}) creó al hijo ({pid})")
    time.sleep(2)  # Dar tiempo para que el hijo termine y se vuelva zombi
    print("Padre finaliza sin llamar a wait()")
    os._exit(0)  # El padre muere, convirtiendo al hijo en huérfano
else:
    print(f"Hijo ({os.getpid()}) inicia y termina rápidamente")
    os._exit(0)  # Hijo muere, pero el padre no lo recoge -> Zombi

