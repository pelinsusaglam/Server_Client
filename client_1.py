import socket

c = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
HOST = "127.0.0.1"
PORT = 6060
ADDR = (HOST,PORT)

c.connect(ADDR)

data = input("kelimeyi gir: \n")
c.send(data.encode())
data1 = c.recv(1024)
print(data1)
print("Sunucudan gelen cevap:", data1.decode())  # Byte formatını tekrar string'e çevir
c.close()