#!/usr/bin/python3

class Demo:
    def __init__(self,data):
        self.storedata = data

    def getdata(self):
        return self.storedata

Demoobj = Demo("Passed data retrived successuflly")
databack = Demoobj.getdata()
print(databack)

