#!/usr/bin/python
import sys

print raw_input("Type any thing which you want to print")

print("Now printing functions available in sys module which are:")

functions = dir(sys)
print functions
