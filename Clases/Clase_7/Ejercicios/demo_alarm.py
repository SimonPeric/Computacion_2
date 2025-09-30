# demo_alarm.py
import signal, time, os

timed_out = False

class TimeoutException(Exception):
    pass

# ---------------- Handlers ----------------
def on_alarm(signum, frame):
    global timed_out
    timed_out = True
    print("[handler] Timeout!")
    raise TimeoutException("⏰ Tiempo de ejecución agotado!")

def handle_signal(signum, frame):
    print("[handler] Señal USR1 recibida!")

# Registrar handlers
signal.signal(signal.SIGALRM, on_alarm)
signal.signal(signal.SIGUSR1, handle_signal)

# Enviar una señal a mí mismo (demostración de SIGUSR1)
signal.raise_signal(signal.SIGUSR1)

# ---------------- Wrapper con timeout ----------------
def run_with_timeout(func, timeout, *args, **kwargs):
    signal.alarm(timeout)   # activar alarma
    try:
        return func(*args, **kwargs)
    finally:
        signal.alarm(0)     # cancelar alarma

# ---------------- Función lenta de ejemplo ----------------
def trabajo_lento():
    print("Trabajo que tarda ~5s...")
    for i in range(5):
        time.sleep(1)
        print(f"  paso {i+1}/5")
    return "✅ Terminé sin timeout"

# ---------------- Reintentos con backoff exponencial ----------------
def run_with_retries(func, timeout, max_retries=3):
    backoff = 1  # primer espera = 1s
    for intento in range(1, max_retries + 1):
        try:
            return run_with_timeout(func, timeout)
        except TimeoutException as e:
            print(f"[intento {intento}] {e}")
            if intento < max_retries:
                print(f"⏳ Esperando {backoff}s antes de reintentar...")
                time.sleep(backoff)
                backoff *= 2  # backoff exponencial
            else:
                print("❌ Falló después de varios intentos")
                raise

# ---------------- Probar ----------------
try:
    resultado = run_with_retries(trabajo_lento, timeout=3, max_retries=4)
    print("Resultado final:", resultado)
except TimeoutException:
    print("Abortando: la tarea nunca terminó a tiempo.")

