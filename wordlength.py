file = open("words.txt","r");
for line in file:
    wordbox = line.split();
    for words in wordbox:
        if(len(words)>10):
            print(words);


