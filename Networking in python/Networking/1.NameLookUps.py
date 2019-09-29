#!/usr/bin/python3

import socket

print(socket.gethostbyaddr("8.8.8.8"))
print(socket.gethostbyname("www.google.com"))
print(socket.gethostbyaddr("172.217.163.68"))


print(socket.gethostbyname("www.facebook.com"))
print(socket.gethostbyaddr("157.240.16.39"))

hostIP = socket.gethostbyname('CyberWorld')  # (hostname or locahost or hostIP,'' )
host2 = socket.gethostbyaddr('127.0.1.1')
print("Getting hostIP by name: ", hostIP)  # means 127.0.1.1
print("Getting host by address: ", host2)
