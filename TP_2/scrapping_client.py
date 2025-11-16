import socket
from common import send_json, recv_json

HOST = "127.0.0.1"
PORT = 9000

def send_request(url):
    s = socket.socket()
    s.connect((HOST, PORT))

    send_json(s, {"url": url})
    response = recv_json(s)

    s.close()
    return response

if __name__ == "__main__":
    url = input("Ingrese URL a scrapear: ")
    res = send_request(url)
    
    print("\n==== RESULTADO FINAL ====")
    print(res)
