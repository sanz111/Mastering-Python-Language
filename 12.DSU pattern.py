#Decorate sort undecorate pattern for sorting words for longest word to shortest word using tuple   
#!/usr/bin/python3

str = "I love Programming. Data Structures and Algorithms are awesome things"
wordsList = str.split()
wordAndLengthList = list()
for word in wordsList:
    wordAndLengthList.append((len(word),word)) #making list of tuples

wordAndLengthList.sort(reverse=True)

for len,word in wordAndLengthList: # traversing tuples in list
    print(word)
