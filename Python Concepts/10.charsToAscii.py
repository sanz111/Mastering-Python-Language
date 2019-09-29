#alphabets with their ascii

#!/usr/bin/python3
capitalDictionay = dict()
smallDictionay = dict()

for i in range(0,26):
    capitalAlpha = chr(i+65)
    smallAlpha = chr(i+97)
    capitalDictionay[capitalAlpha] = i+65
    smallDictionay[smallAlpha] = i+97

print("Capiltal letters with their ASCII:")
print(capitalDictionay)
print("Small letters with their ASCII:")
print(smallDictionay)