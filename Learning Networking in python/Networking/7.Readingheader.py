#!/usr/bin/python

import pcapy
from struct import *

captured_data = pcapy.open_live("wlp6s0",65536,1,0)

while 1:
    (header,payload) = captured_data.next()
    layer2hdr = payload[0:14]
    layer2data = unpack("!6s6sH",layer2hdr)

    srcmac = "%.2x:%.2x:%.2x:%.2x:%.2x:%.2x:" %(ord(layer2hdr[0]), ord(layer2hdr[1]), ord(layer2hdr[2]), ord(layer2hdr[3]), ord(layer2hdr[4]), ord(layer2hdr[5]))
    dstmac = "%.2x:%.2x:%.2x:%.2x:%.2x:%.2x:" %(ord(layer2hdr[6]), ord(layer2hdr[7]), ord(layer2hdr[8]), ord(layer2hdr[9]), ord(layer2hdr[10]), ord(layer2hdr[11]))
    print("Source MAC:",srcmac, "Destination MAC:",dstmac)

    ipheader = unpack('!BBHHHBBH4s4s', payload[14:34])
    timetolive = ipheader[5]
    protocol = ipheader[6]

    print("protoccol", str(protocol), "Time to live: ",str(timetolive))
    print('')