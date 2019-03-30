#!/usr/bin/python3


import ftplib

server = "ftp.gmail.com"
sender = "firojvsfacebook@gmail.com"
password = "mummy14343ver"
f = ftplib.FTP(server)

try:
    f.login(sender,password)
    print(f.getwelcome())
    #f.delete("myfile")
    print(f.dir())
    f.set_pasv(1)
    f.storbinary("STOR myfile", open("myfile", "rb"))
    print(f.dir())
except Exception as e:
    print("Exception: ", e)
finally:
    f.close()
