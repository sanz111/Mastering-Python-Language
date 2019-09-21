from collections import Counter
#it is just another approach of counting words,chars, numbers and so on unsing Counter
counting = Counter()
FNAME = input("Enter the name of the file\n")
FILE1 = open(FNAME, "r+")
N = int(input("First how many lines you want to display\n"))
FIRSTLINES = FILE1.readlines()[0:N]
print(FIRSTLINES)
FILE1.close()

FILE1 = open(FNAME, "r+")
for line in FILE1:
    wordsList = line.split()
    for word in wordsList:
        counting[word] = counting[word]+1
print(counting)
FILE1.close()
