import socket

s = socket.socket()
host = ""  #ip address of machine running server.py read readme.txt to see how
port = 5000
s.connect(('127.0.0.1', port))
message = s.recv(1024)
print("server : " + message.decode())
message = input(" -> ")

while message.lower().strip() != 'bye':
    s.send(message.encode())
    message = s.recv(1024)
    print("server : " + message.decode())
    message = input(" -> ")
