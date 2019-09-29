# count occurances of each character in a string
# technique: making char as index and charCount as value
#  dic[key] = value => update the dictionary with corresponding value to the key.

str = "firojyouareawesome"
d = dict()

for key in str:
    if key not in d:
        d[key] = 1  # initializing {'f':1,...}
    else:
        d[key] = d[key]+1

print("without get() method \n", d)

for key in str:
    d[key] = d.get(key, 0) + 1

print("without get(key,default_value) method \n", d)
