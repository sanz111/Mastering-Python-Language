#!/usr/bin/python3
# object oriented-concept with life cycle methods like __init__(), userMethods(), __del__()

class Demo:
    def __init__(self,data):
        print("Constructor gets callled automatically")
        self.data = data

    def setdata(self,data):
        self.data  = data

    def getdata(self):
        return self.data


    def __del__(self):
        print("Destructor gets callled automatically")

o1 = Demo("data1") 
print(o1.getdata())

o2 = Demo("data2")
print(o2.getdata())
o2.setdata("data3")
print(o2.getdata())


# when a class is instancialized, it calls constructor method automatically for
# initializing instance variables(variables common to all methods).

# And When that instance of the class(OBJECT) finishes doing all its works(behaviour) then at the
# end only the deconstructor of that instance is called for releasing alloted resources.

# NOTE: if there is only one instance of a class then no. of calls for constructor and destructor 
# will also be only one. CALLS PER CONSTRUCTOR & DECONSTRUCTOR = no. of instances