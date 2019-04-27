#!/usr/bin/python3

import socket

SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

SERVER_IP = input("Enter the Server IPaddess you want to connect: ")
SERVER_PORT = int(input("Enter the Port no. Server is Operating on: "))
ADDRESS = (SERVER_IP, SERVER_PORT)

try:
    print("Trying to Connect.... ", ADDRESS)
    SOCKET.connect(ADDRESS)
    print("Connection Successful\n")
    MESSAGE = input("Enter the Message you want to send :\n")
    SOCKET.sendall(MESSAGE.encode('utf-8'))
    print("Message sent")
except Exception as E:
    print(E)
finally:
    SOCKET.close()
