#!/usr/bin/python3

import socket

SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SOCKET.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

HOST = ''
PORT = 5555
SOCKET.bind((HOST, PORT))
print("Server Started...Listening....\n")
SOCKET.listen(5)  # no.of simultaneous connections

CLIENTSOCKET, CLIENTADDRESS = SOCKET.accept()
print("Connection Established with: ", CLIENTADDRESS)

DATA = CLIENTSOCKET.recv(512)

if DATA:

    print("DATA RECEIVED IS:\n", DATA.decode("utf-8"))
    f = open("storage.dat", "w")
    print("Also the DATA has been saved to the file storage.dat\n")
    f.write(CLIENTADDRESS[0])
    f.write(":")
    f.write(DATA.decode("utf-8"))
    f.close()

SOCKET.close()
