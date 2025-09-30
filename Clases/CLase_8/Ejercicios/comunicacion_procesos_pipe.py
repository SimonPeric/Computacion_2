from multiprocessing import Process, Pipe

def enviar_msg(conn):
    conn.send("Hola desde el hijo")
    conn.close()

def recibir_msg(conn):
    msg = conn.recv()
    print(f"Mensaje recibido: {msg}")
    conn.close()

if __name__ == "__main__":
    padre_conn, hijo_conn = Pipe()
    
    p1 = Process(target=enviar_msg, args=(hijo_conn,))
    p2 = Process(target=recibir_msg, args=(padre_conn,))
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
