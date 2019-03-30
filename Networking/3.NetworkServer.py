#!/usr/bin/python3

import socket

size = 512 #bytes we expect to receive
host = ''
port = 9898

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

sock.bind((host,port))
sock.listen(5)

c, address = sock.accept()
data = c.recv(size)

if data:
    f = open("storage.dat","w")
    print("Connection is from", address[0])
    f.write(address[0])
    f.write(":")
    f.write(data.decode("utf-8"))
    f.close()

sock.close()