#!/usr/bin/python3


def compressString(s):
    result = ''
    length = len(s)

    if length == 0:
        return ''

    if length == 1:
        return s+"1"

    count = 1
    i = 1

    while i < length:
        if s[i] == s[i-1]:
            count += 1
        else:
            result = result + s[i-1] + str(count)
            count = 1
        i += 1
    result = result + s[i-1] + str(count)
    return result


if __name__ == "__main__":
    print(compressString("ABBCCCB"))
