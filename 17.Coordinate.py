#!/usr/bin/python3

# It's an example from MIT
#Every class INHERIT object class by default even if not specified.

class Cordinate(object):
    """ finds distance between two cordinates"""
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    # distance = (x-x1)**2 + (y=y1)**2
    def distance(self, other):
        x_diff_sq = (self.x-other.x)**2
        y_diff_sq = (self.y-other.y)**2
        return (x_diff_sq + y_diff_sq)
    
    def __str__(self):
        return "<"+str(self.x)+","+str(self.y)+">"

c = Cordinate(3,4)
zero = Cordinate(0,0)
#See it looks like list object, list1.append(list2)
print(c.distance(zero))



#type() method gives which class an instance(object) belongs to
print(isinstance(c, Cordinate))
print(c)
print(Cordinate)

#NOTE: Every CLASS is an INSTANCE(OBJECT) of class TYPE
# E.g here even Cordinate class is an instance(object) of class type which 
# means Cordinate class acts type for its object.
print(type(c))
print(type(Cordinate))
