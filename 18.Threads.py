#!/usr/bin/python3

import threading

class ThreadDemo(threading.Thread):
    def __init__(self,num,val):
        threading.Thread.__init__(self)
        self.threadNum = num
        self.loopCount = val

    def run(self):
        print("Starting run: ",self.threadNum)
        myfunction(self.threadNum,self.loopCount)

def myfunction(num,val):
    count = 0
    while count < val:
        print(num,":",val*count)
        count = count + 1


t1 = ThreadDemo(1,15)
t2 = ThreadDemo(2,20)
t3 = ThreadDemo(3,25)
t4 = ThreadDemo(4,30)

# Now starting all Created Threads

t1.start()
t2.start()
t3.start()
t4.start()

# now we are going to join all running threads and a collection
# so now defining a collection array first

threads = [] # contains array of threads running
threads.append(t1)
threads.append(t2)
threads.append(t3)
threads.append(t4)

for t in threads:
    t.join()




