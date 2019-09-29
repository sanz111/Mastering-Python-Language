#!/usr/bin/python3

d = dict()
file = open("words.txt","r")
wordsList = list()
charsList = list()

for line in file:
    wordsList = line.split()
# print(wordsList)  but why??????
    for word in line:
        for char in word:
            if char not in d:
                d[char] = 1
            else:
                d[char] = d[char] + 1
print(d)

# for line in file:
#     print(line)
#     wordsList = line.split()
#     print(wordsList)

#     for word in wordsList:
#         charsList = list(word)
#         print(charsList)

#         for char in charsList:
#             if char not in d:
#                 d[char] = 1
#             else:
#                 d[char] = d[char] + 1
# print(d)
        