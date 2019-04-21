from collections import Counter

cnt = Counter()
FNAME = input("Enter the name of the file\n")
FILE1 = open(FNAME, "r+")
N = int(input("First how many lines you want to display\n"))
FIRSTLINES = FILE1.readlines()[0:N]
print(FIRSTLINES)
FILE1.close()

FILE1 = open(FNAME, "r+")
for line in FILE1:
    for word in line.split():
        cnt[word] = cnt[word]+1
print(cnt)
FILE1.close()
