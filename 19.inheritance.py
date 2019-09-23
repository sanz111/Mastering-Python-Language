#!/usr/bin/python3

# GLOBAL VARIABLES: Variable set outside __init__ belong to the class. They're shared by all the methods 
# of the instances i.e (GLOBAL_TO_THE_WHOLE_CLASS) so also called CLASS_VARIABLES/INSTANCE_VARIABLES

# PRIVATE VARIABLES: Variables are created inside methods and can be accessed from inside
# the method only. If variables are declared inside __init__() method, though those variables being private,
# other methods inside the same class, can access those private_variables using SELF keyword.


#METHOD 1 (GLOBAL VARIABLES)
# Using parent_class_name instead of parent_class_instance for accessing instance_variable of parent class

class parent1:
    a = 20
    b = 30
    
class child1(parent1):

    def add(self):
        self.sum = parent1.a + parent1.b
        print(self.sum)

if __name__ == "__main__":
    
    c1 = child1()
    c1.add() #working because variables are initialized outside __init__()



# METHOD 2 (GLOBAL VARIABLES)
# for accessing instance variable of parent class, parent_class_instance should be passed to child methods as argument.

class parent2:
    a = 20
    b = 30
    
class child2(parent2):

    def add(self, p2):
        self.sum = p2.a + p2.b
        print(self.sum)

if __name__ == "__main__":
    
    c2 = child2()
    p2 = parent2()
    c2.add(p2) # this way works no matter variables are initialized INSIDE or OUTSIDE __init__()



#__init__() method(Constructor) used to declare & initialize private_variables for each instance saperately inside it.

class parent3:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        self.sum = self.a + self.b
        print(self.sum)


if __name__ == "__main__":
    
    p3 = parent3(20,30)
    p3.add()
    p4 = parent3(70,30)
    p4.add()


# Now Using child_class __init__(constructor) to overide value of parent's private_variables.
class parent5:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return "<"+str(self.a)+","+str(self.b)+">"

class child5(parent5):

    def __init__(self,c,d):
        super().__init__(c,d)

    def add(self):
        self.sum = self.a + self.b
        print(self.sum)

p5 = parent5(20,30)
print(p5)


c5 = child5(70,30)
c5.add()
c6 = child5(90,30)
c6.add()