#!/usr/bin/python3

class Demo:
    def __init__(self,data):
        self.storedata = data

    def getdata(self):
        return self.storedata

    def setdata2(self,data2):
        self.storedata2  = data2

d1 = Demo("d1")
d2 = Demo("d2")
d3 = Demo("d3")
d3.__init__("d4") # reassining value of storedata

print(d1.getdata()) # m1 this is being returned by getdata method
print(d2.storedata) # m2 this value is directly being extracted from storedata variable
print(d3.getdata())

d1.setdata2("d5")
print(d1.storedata2) # same m2 type

