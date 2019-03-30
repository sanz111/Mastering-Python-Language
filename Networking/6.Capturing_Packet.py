#!/usr/bin/python3

import pcapy

devices = pcapy.findalldevs()
print(devices)

captured_data = pcapy.open_live("wlp6s0",65536,1,0) #(interface,bytes per packet,monitor mode, ms timeout)

count = 1
while True:
    (header,payload) = captured_data.next()
    print(count)
    count = count + 1

