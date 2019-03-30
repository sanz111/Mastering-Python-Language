#!/usr/lib/python3

import os
from subprocess import call

print(os.getcwd())
print(os.getuid())
print(os.getenv("PATH"))
os.system("ls -la")

input = input("Hit Enter")

call(["ls","-la"])
