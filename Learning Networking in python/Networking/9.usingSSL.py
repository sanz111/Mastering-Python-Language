#!/usr/bin/python
import ssl
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # created socket
ssock = ssl.wrap_socket(s)

try:
    s.connect(("www.google.com", 443))
    print(ssock.cipher())
except:
    print("Communication error")

try:
    ssock.write(b"GET / HTTP/1.1 \r\n")
    ssock.write(b"Host: www.google.com\n\n")
except Exception as e:
    print("Write error:",e)

data = bytearray()
try:
    data = ssock.read()
except Exception as e:
    print("read error:", e)

print(data.decode("utf-8"))