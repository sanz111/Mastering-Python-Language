#!/usr/bin/python3

import string

d1 = dict.fromkeys(string.ascii_lowercase)
# d2 = dict.fromkeys(string.ascii_uppercase)
# d3 = dict.fromkeys(string.ascii_letters)

for key in d1:
    d1[key] = ord(key)
print(d1)