#!/usr/bin/python3

'''
What is POLYMORPHISM ?
> Generally INHERITANCE is utilized to create POLYMORPHISM which means ‘a state of having many shapes’ or 
  ‘the capacity to take on different forms or behaviour’.
'''

# In OOP, Polymorphism means a subclass can override a method of the base class


''' 
1) Dynamic/Duck-Type Polymorphism :
-----------------------------------
* METHOD OVERRIDING (Run-time-binding) :
>  Happens if Same Method_name in DIFFERENT_CLASS
> It is useful where the method inherited from the parent class doesn’t quite fit the child class.
> In such cases, we re-implement(override) the method in the child class 
'''


class Shape:

    def intro(self):
        print("I am Shape")

    def area(self):
        print("Area of a shape refers to the 2D space occupied by the shape")


class Rectangle(Shape):
    def area(self, length, breadth):
        print("area of rectangle is: %d" % (length*breadth))


class Circle(Shape):
    def area(self, radius):
        print("Area of circle is: %d" % (3.14*radius*radius))


s1 = Shape()
s1.intro()
s1.area()

r1 = Rectangle()
s1.intro()
r1.area(20, 10)

c1 = Circle()
s1.intro()
c1.area(7)

'''
2) STATIC/Sub-type Polymorphism : is achieved through Method OverLoading.
---------------------------------
* METHOD OVERLOADING (Compile-time-binding) :
> Happens if Same Method_name in SAME_CLASS 
> NOTE: This is NOT_POSSIBLE in python because python is dynamically-typed. If multiple methods have 
        been declared inside one class, python takes only one and LAST_METHOD.
 
'''

print("Static Polymorphism not possible in python\n----------------------------")


class Shape:

    def intro(self):
        print("I am Shape")

    def area(self):
        print("Area of a shape refers to the 2D space occupied by the shape")

    def area(self, length, breadth):
        print("area of rectangle is: %d" % (length*breadth))

    def area(self, radius):  # this method will only be considered
        print("Area of circle is: %d" % (3.14*radius*radius))


s1 = Shape()
s1.intro()
s1.area(7)
s1.area()  # will not work because we are not passing radius argument.
s1.area(20, 10)
