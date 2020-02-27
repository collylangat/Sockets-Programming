import socket

server = socket.socket()
port = 5000
server.bind(('', port))
server.listen(10)
while True:
    sock, client_address = server.accept()
    sock.send("Hello".encode())
    print("server connected to " + str(client_address))
    while True:
        client_mes = sock.recv(1024)
        sock.send(client_mes)
