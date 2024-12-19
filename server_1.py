import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
HOST = "127.0.0.1"
PORT = 6060
ADDR = (HOST,PORT)

s.bind(ADDR)

def start():
    s.listen()
    print("listening...")
    while True:
        conn, addr = s.accept()
        print(f"{addr} bağlandı.")
        data = conn.recv(1024)
        if not data:
            break
        data1 = data.upper()
        conn.send(data1)
        conn.close()
start()