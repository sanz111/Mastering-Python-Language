#!/usr/bin/python3

import socket

SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SOCKET.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


def LocalIP():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = socket.gethostbyname(socket.gethostname())
        # IP = '127.0.1.1'
    finally:
        s.close()
    return IP


SERVER_IP = LocalIP()
SERVER_PORT = 5555
SOCKET.bind((SERVER_IP, SERVER_PORT))
SOCKET.listen(5)  # no.of simultaneous connections
print("Server Started...Listening....at", SERVER_IP, SERVER_PORT)

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
