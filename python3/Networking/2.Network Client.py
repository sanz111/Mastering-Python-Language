#!/usr/bin/python3

import  socket

host = 'localhost' # means 127.0.0.1
port = 5555
address = (host,port)

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(address)
try:
    msg = b"This is test message being sent through TCP\n"
    client.sendall(msg)
except socket.errno as e:
    print("Socket error", e)
finally:
    client.close()
