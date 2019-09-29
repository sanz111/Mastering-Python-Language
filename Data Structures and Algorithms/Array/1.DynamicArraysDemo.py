#!/usr/bin/python3

'''
Demonstrating How the size of a list grows dynamicaly 
when the elements in the list increases at run time.
'''
import sys

n = 15  # no. being appended to the list one by one
myList = []
for i in range(n):
    currentLength = len(myList)
    actualSize = sys.getsizeof(myList)
    print("Current Length of list is %d, and its Size in bytes is %d" %
          (currentLength, actualSize))
    myList.append(n)
