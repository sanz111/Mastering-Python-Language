#!/usr/bin/python3

import copy

'''
There are two types of copy:

1. Shallow copy (=):
> Copies the REFERENCE(hard link/memory-address) of an object and assigns to another object. 
> Even when we use assign operator (=), it performs the same shallow copy.so difference in using copy.copy() method and = operator
> Hence changes made in one object will reflect in another as they are pointing to the same data/memory-address
> 
'''
print("Everything in python is object")
print("This a is also an object from int class")
a = 15
print(type(a))

b = a  # shalow copy
c = copy.copy(a)  # it also performs shallow copy
print(id(a))
print(id(b))
print(id(c))

'''
2. Deep copy:
> copies the DATA, creates a new object and assigns that data to the new object.
> Now both old and new objects are now two difference object of same type and holding the same data in different memory location.
> Hence Changes made in one object will not affect the data of another object.

'''

d = copy.deepcopy(a)
print(id(d))
