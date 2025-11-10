import socket
import json

HOST = '127.0.0.1'
PORT = 8000

data = {"text": "Hola mundo distribuido con sockets y threading"}

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.send(json.dumps(data).encode('utf-8'))
    response = s.recv(4096).decode('utf-8')
    print("Respuesta del servidor:")
    print(json.loads(response))
