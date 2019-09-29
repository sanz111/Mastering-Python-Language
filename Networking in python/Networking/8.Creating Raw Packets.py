#!/usr/bin/python
from scapy.all import *

packet = Ether(dst= "15:8a:33:3f:9d:32")/IP(dst= "9.16.5.4")/TCP()/"This is my payload"


print(packet)
send(packet)
