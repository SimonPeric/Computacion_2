import socket
import threading
from common import send_json, recv_json
import requests

HOST = "127.0.0.1"
PORT = 9000

PROCESS_HOST = "127.0.0.1"
PROCESS_PORT = 9001

def fake_scrape(url):
    """Simula scrapping (por entrega)"""
    return f"Contenido simulado de la URL: {url}"

def send_to_processing(text):
    s = socket.socket()
    s.connect((PROCESS_HOST, PROCESS_PORT))
    send_json(s, {"text": text})
    result = recv_json(s)
    s.close()
    return result

def handle_client(conn, addr):
    print(f"[SCRAPPING] Cliente conectado: {addr}")

    try:
        request = recv_json(conn)
        print(f"[SCRAPPING] Petición recibida: {request}")

        url = request.get("url")

        scraped = fake_scrape(url)
        print("[SCRAPPING] Texto scrapado:", scraped)

        result = send_to_processing(scraped)
        print("[SCRAPPING] Resultado procesamiento:", result)

        send_json(conn, result)

    except Exception as e:
        print(f"[ERROR SCRAPPING] {e}")

    conn.close()

def start_server():
    print("[SCRAPPING] Servidor iniciado en puerto 9000")
    s = socket.socket()
    s.bind((HOST, PORT))
    s.listen()

    while True:
        conn, addr = s.accept()
        threading.Thread(target=handle_client, args=(conn, addr)).start()

if __name__ == "__main__":
    start_server()
