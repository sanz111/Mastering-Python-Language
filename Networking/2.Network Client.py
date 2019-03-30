#!/usr/bin/python3

import  socket

hostIP = socket.gethostbyname('CyberSecurityExpert') #(hostname or locahost or hostIP, '' )
host2 = socket.gethostbyaddr('127.0.1.1')
print("Getting hostIP by name: ",hostIP) # means 127.0.1.1
print("Getting host by address: ",host2)

port = 5555
address = (hostIP,5555)

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(address)
try:
    msg = b"This is test message being sent through TCP\n"
    client.sendall(msg)
except socket.errno as e:
   print("Socket error", e)
finally:
    client.close()
