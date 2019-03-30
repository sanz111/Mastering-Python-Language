#!/usr/bin/python3

x = int(input("Enter any number "))

if(x<1):
    print(str(x) + " is less than 1")
elif(x >= 1 and x <= 10):
    print(str(x) +" is between 1 and 10")
else:
    print(str(x) + " is greater than 10")
