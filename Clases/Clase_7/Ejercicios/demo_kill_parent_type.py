# demo_kill_parent_child.py
import os, time, signal, sys

def child():
    print(f"[child] PID={os.getpid()} esperando señal...")
    def on_usr1(signum, frame):
        print(f"[child] Recibí SIGUSR1 ({signum}). ¡Sigo!")
        sys.exit(0)
    signal.signal(signal.SIGUSR1, on_usr1)
    while True:
        time.sleep(0.5)

def parent():
    pid = os.fork()
    if pid == 0:
        child()
    else:
        print(f"[parent] Enviando SIGUSR1 a hijo {pid} en 2s...")
        time.sleep(2)
        os.kill(pid, signal.SIGUSR1)
        os.waitpid(pid, 0)
        print("[parent] Hijo terminó.")

if __name__ == "__main__":
    parent()
