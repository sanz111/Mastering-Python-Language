#!/usr/bin/python3

#Variable set outside __init__ belong to the class. They're shared by all instances.(GLOBAL_TO_THE_WHOLE_CLASS)
# Variables created inside __init__ (and all other method functions) and accessed with self always, 
# and belong to the object instance.(GLOBAL_TO_EACH_INSTANCE_OF_THE_CLASS)

#METHOD 1
# Using parent_class_name instead of parent_class_instance for accessing instance variable of parent class

class parent1:
    a = 20
    b = 30
    
class child1(parent1):

    def add(self):
        self.sum = parent1.a + parent1.b
        print(self.sum)

if __name__ == "__main__":
    
    c1 = child1()
    c1.add() #works because variables are outside __init__()



# METHOD 2
# for accessing instance variable of parent class, parent_class_instance should be passed to child methods as argument.

class parent2:

    def __init__(self):
        self.a = 20
        self.b = 30
    
class child2(parent2):

    def add(self, p2):
        self.sum = p2.a + p2.b
        print(self.sum)

if __name__ == "__main__":
    
    c2 = child2()
    p2 = parent2()
    c2.add(p2)
