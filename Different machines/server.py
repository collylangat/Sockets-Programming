import socket

server = socket.socket()
host = ""  # ip address of machine running server.py read readme.txt to see how
port = 5000
server.bind((host, port))
server.listen(10)
while True:
    sock, client_address = server.accept()
    print("server connected to " + str(client_address))
    sock.send("Hello".encode())
    while True:
        client_mes = sock.recv(1024)
        print("Client : " + client_mes.decode())
        message = input(" -> ")
        sock.send(message.encode())
