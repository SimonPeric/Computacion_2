import socket
import threading
import json

HOST = '127.0.0.1'
PORT = 8000
PROCESSING_HOST = '127.0.0.1'
PROCESSING_PORT = 8001

def request_processing_server(data):
    """Se comunica con el servidor de procesamiento (B)"""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((PROCESSING_HOST, PROCESSING_PORT))
        s.send(json.dumps(data).encode('utf-8'))
        response = s.recv(4096).decode('utf-8')
        return json.loads(response)

def handle_client(conn, addr):
    print(f"[NUEVA CONEXIÓN CLIENTE] {addr}")
    try:
        data = conn.recv(4096).decode('utf-8')
        if not data:
            return

        request = json.loads(data)
        print(f"[PETICIÓN CLIENTE] {request}")

        # Enviamos parte del trabajo al servidor B
        processing_result = request_processing_server(request)

        # Construimos respuesta final
        result = {
            "original_text": request.get("text", ""),
            "processing_result": processing_result,
            "status": "success"
        }

        conn.send(json.dumps(result).encode('utf-8'))
        print(f"[RESPUESTA AL CLIENTE] {result}")
    except Exception as e:
        print(f"[ERROR] {e}")
    finally:
        conn.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print(f"[SERVIDOR A - Scraping] Escuchando en {HOST}:{PORT}")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVAS] {threading.active_count() - 1} clientes")

if __name__ == "__main__":
    start_server()
