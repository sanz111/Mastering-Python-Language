#!/usr/bin/python3

import socket
import re

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # creating a tcp objectd
sock.connect(("WWW.microsoft.com",80))

http_get = b"GET / HTTP/1.1\nHost: www.microsoft.com\n\n"
data = ''

try:
    sock.sendall(http_get)
    data =sock.recvfrom(1024)
except socket.error:
    print("Socket error",socket.errno)
finally:
    print("closing connection")
    sock.close()

stringdata = data[0].decode("utf-8")
headers = stringdata.splitlines()

for s in headers:
    if re.search('Server:',s):
        s = s.replace("Server: ", " ")
        print(s)


