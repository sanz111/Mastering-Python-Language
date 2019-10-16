#!/usr/bin/python3


def uniqueChars1(s):
    return len(set(s)) == len(s)


def uniqueChars2(s):
    uniqueList = list()

    for letter in s:
        if letter in uniqueList:
            return False
        else:
            uniqueList.append(letter)
    return True


if __name__ == "__main__":
    print(uniqueChars2("abcde"))
