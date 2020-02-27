import socket
import sys
#create socket
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket created")
except socket.error as err:
    print("socket not created because of " + err)
port = 80

#connect to server
try:
    host = socket.gethostbyname("www.google.com")

except socket.gaierror as er:
    print("could not connect to server ")
    print(er)
    sys.exit()

s.connect((host, port))
print("socket has been connected to server vie port " +host)