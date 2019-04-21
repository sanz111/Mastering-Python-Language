fname = open("words.txt", "r")
dic = dict()
for line in fname:
    word = line.split()  # better to use it in case multiple words are there in one line
    for word in line:
        char = list(word)
        for letter in char:
            if(letter in dic):
                dic[letter] = dic[letter]+1
            else:
                dic[letter] = 1
print(dic)
