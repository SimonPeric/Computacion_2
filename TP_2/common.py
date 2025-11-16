import json

def send_json(conn, data):
    message = json.dumps(data).encode()
    conn.sendall(len(message).to_bytes(4, 'big') + message)

def recv_json(conn):
    length = int.from_bytes(conn.recv(4), 'big')
    data = conn.recv(length)
    return json.loads(data.decode())
