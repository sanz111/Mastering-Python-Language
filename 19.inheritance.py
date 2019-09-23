#!/usr/bin/python3


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
    c1.add()



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
