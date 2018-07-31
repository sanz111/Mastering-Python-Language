#!/usr/bin/env python

import threading
import time

def myfunction():
	print "Started a thread"
	time.sleep(3)
	print "Ended the thread"
	
threads = []

for i in range(5):
    th = threading.Thread(target = myfunction)
    th.start()
    threads.append(th)

for i in threads:
    th.join()
    print "joined by:",th
