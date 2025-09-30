# demo_threads_signal.py
import signal, threading, time

stop = threading.Event()

def worker(i):
    while not stop.is_set():
        # trabajo simulado
        time.sleep(0.2)
    print(f"[worker {i}] cierre ordenado")

def on_sigint(signum, frame):
    stop.set()

signal.signal(signal.SIGINT, on_sigint)

threads = [threading.Thread(target=worker, args=(i,), daemon=True) for i in range(3)]
[t.start() for t in threads]
print("Hilos trabajando. Presiona Ctrl+C para detener.")
[t.join() for t in threads]  # terminarán cuando stop esté set
