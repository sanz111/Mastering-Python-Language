#!/usr/bin/python3

import socket

size = 512
host = ''
port = 9898

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
sock.listen(5)

client, addr = sock.accept()
data = client.recv()

if data:
    f = open("storage.dat","w")
    print("Connection is from", addr[0])
    f.write(addr[0])
    f.write(":")
    f.write(data.decode("utf-8"))
    f.close()

sock.close()