#!/usr/bin/python
import os
myuid = os.getuid()
if myuid == 0:
    print("you are root user")
elif myuid < 500:
    print("you are a system account user")
else:
    print("you are just a regular user")
