# demo_sync_signal_mp.py
import os, time, signal, multiprocessing as mp

# Evento global por proceso (no compartido entre procesos, cada proc tiene su copia)
released = mp.Event()

def on_usr1(signum, frame):
    released.set()

def worker():
    signal.signal(signal.SIGUSR1, on_usr1)
    print(f"[worker {os.getpid()}] Esperando señal SIGUSR1 para iniciar...")
    # bucle hasta que llegue la señal
    while not released.is_set():
        time.sleep(0.1)
    print(f"[worker {os.getpid()}] ¡Recibí señal! Empezando trabajo...")
    time.sleep(1)
    print(f"[worker {os.getpid()}] Trabajo terminado.")

if __name__ == "__main__":
    p = mp.Process(target=worker)
    p.start()
    time.sleep(1)
    print(f"[parent {os.getpid()}] Enviando SIGUSR1 a {p.pid}")
    os.kill(p.pid, signal.SIGUSR1)
    p.join()
    print("[parent] Listo.")
