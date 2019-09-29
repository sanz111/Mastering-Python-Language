#!/usr/bin/python3
# Anagram is when two strings can be written using same string letters.

# MY_VERSION


def removeSpace(str):
    newstring = ""
    for i in str:
        if i == ' ':
            continue
        else:
            newstring = newstring + i
    return newstring


def isAnagram(str1, str2):
    str1 = removeSpace(str1)
    str2 = removeSpace(str2)
    if len(str1) != len(str2):
        return False

    for i in str1:
        if i not in str2:
            return False
        continue
    return True


def isAnagram2(str1, str2):
    str1 = str1.replace(" ", "")
    str2 = str2.replace(" ", "")
    return sorted(str1) == sorted(str2)


def isAnagram3(str1, str2):

    if len(str1) != len(str2):
        return False

    d = dict()
    for letter in str1:
        if letter not in d:
            d[letter] = 1
        else:
            d[letter] = d[letter]+1

    for letter in str2:
        if letter not in d:
            d[letter] = 1
        else:
            d[letter] = d[letter]-1

    # looping through the values of dictionary
    for i in d:
        if d[i] != 0:
            return False
    return True


if __name__ == "__main__":
    a = "firoj"
    b = "fijor"
    if isAnagram(a, b) and isAnagram(b, a):
        print("Both Strings are anagram")
    else:
        print("Not an Anagram")

    print(isAnagram2(a, b))
    print(isAnagram3(a, b))
