FILE1 = open("parseme.txt", "r")
for line in FILE1:
    if not line.startswith("from"):
        continue
    words = line.split()
    print(words[2])
