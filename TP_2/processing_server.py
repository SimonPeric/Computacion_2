import socket
import threading
from common import send_json, recv_json

HOST = "127.0.0.1"
PORT = 9001

def process_data(data):
    """Simula procesamiento biométrico con blockchain local."""
    text = data.get("text", "")

    result = {
        "original": text,
        "length": len(text),
        "checksum": sum(ord(c) for c in text) % 256
    }
    return result

def handle_client(conn, addr):
    print(f"[PROCESSING] Cliente conectado: {addr}")

    try:
        request = recv_json(conn)
        print(f"[PROCESSING] Datos recibidos: {request}")

        result = process_data(request)

        send_json(conn, result)
        print(f"[PROCESSING] Enviado resultado.")
        
    except Exception as e:
        print(f"[ERROR PROCESSING] {e}")

    conn.close()

def start_server():
    print("[PROCESSING] Servidor iniciado en puerto 9001")
    s = socket.socket()
    s.bind((HOST, PORT))
    s.listen()

    while True:
        conn, addr = s.accept()
        threading.Thread(target=handle_client, args=(conn, addr)).start()

if __name__ == "__main__":
    start_server()
