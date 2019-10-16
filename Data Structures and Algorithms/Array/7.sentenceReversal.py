#!/usr/bin/python3

def reverseSentence1(sentence):
    return " ".join(reversed(sentence.split()))

def reverseSentence2(sentence):
    return " ".join(sentence.split()[::-1])

def reverseSentence3(sentence):
    length = len(sentence)
    words = []
    space = [' ']

    def splitIntoWords(sentence):
        i = 0
        while i < length:
            if sentence[i] not in space:
                wordStart = i

                #traversing one word
            while i < length and sentence[i] not in space:
                i += 1
            words.append(sentence[wordStart:i])
            i += 1
        return words
        
    def reverseArray(words):
        revArray = []
        i = len(words)-1
        while(i >= 0):
            revArray.append(words[i])
            i -= 1
        return revArray

    return " ".join(reverseArray(splitIntoWords(sentence)))
        
            

if __name__ == "__main__":
    print(reverseSentence3("i love python"))