#!/usr/bin/python3

import socket

SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

SERVER_IP = '192.168.1.9'  # SOCKET.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
SERVER_PORT = 5555  # Port on which target or server or other client is listening
ADDRESS = (SERVER_IP, SERVER_PORT)

try:
    print("Trying to Connect....\n")
    SOCKET.connect(ADDRESS)
    print("Connection Successful\n")
    MESSAGE = b"This is test message being sent through TCP\n"
    SOCKET.sendall(MESSAGE)
    print("Message sent")
except Exception as E:
    print("Socket error! Server might be down", E)
finally:
    SOCKET.close()
