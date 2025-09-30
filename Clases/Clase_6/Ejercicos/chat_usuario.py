import os
import sys
import threading

def recibir_mensajes(fifo_rx):
    """Lee mensajes del FIFO de recepción."""
    if not os.path.exists(fifo_rx):
        os.mkfifo(fifo_rx)
    with open(fifo_rx, "r") as fifo:
        for linea in fifo:
            print(f"\n📩 Mensaje recibido: {linea.strip()}\n> ", end="")

def enviar_mensajes(fifo_tx):
    """Envía mensajes al FIFO de transmisión."""
    while True:
        mensaje = input("> ")
        with open(fifo_tx, "w") as fifo:
            fifo.write(mensaje + "\n")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python3 chat_usuario.py <mi_fifo> <fifo_destino>")
        sys.exit(1)

    fifo_rx = sys.argv[1]  # FIFO para recibir mensajes
    fifo_tx = sys.argv[2]  # FIFO del otro usuario

    # Hilo para recibir mensajes
    hilo_rx = threading.Thread(target=recibir_mensajes, args=(fifo_rx,), daemon=True)
    hilo_rx.start()

    # Bucle principal: enviar mensajes
    enviar_mensajes(fifo_tx)
