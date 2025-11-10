import socket
import threading
import json

HOST = '127.0.0.1'  # Escucha solo localmente
PORT = 8001         # Puerto del servidor B

def handle_client(conn, addr):
    print(f"[NUEVA CONEXIÓN] {addr} conectado.")
    try:
        data = conn.recv(4096).decode('utf-8')
        if not data:
            return
        
        # Deserializamos el mensaje recibido (JSON)
        request = json.loads(data)
        print(f"[SOLICITUD RECIBIDA] {request}")

        # Simulamos procesamiento pesado
        text = request.get("text", "")
        response = {
            "uppercase": text.upper(),
            "length": len(text)
        }

        # Devolvemos la respuesta serializada
        conn.send(json.dumps(response).encode('utf-8'))
        print(f"[RESPUESTA ENVIADA] {response}")
    except Exception as e:
        print(f"[ERROR] {e}")
    finally:
        conn.close()
        print(f"[DESCONECTADO] {addr}")

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print(f"[SERVIDOR B - Procesamiento] Escuchando en {HOST}:{PORT}")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVAS] {threading.active_count() - 1} conexiones")

if __name__ == "__main__":
    start_server()
