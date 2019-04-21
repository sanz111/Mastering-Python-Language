
fname = open("words.txt", "r")
dic = dict()
for line in fname:
    word = line.split()  # better to use it in case multiple words are there in one line
    for w in word:
        if(w in dic):
            dic[w] = dic[w] + 1
        else:
            dic[w] = 1
print (dic)
