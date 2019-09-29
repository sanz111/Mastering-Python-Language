str = input("Enter String:")
count = 0

for i in str:
    if i in ['a', 'e', 'i', 'o', 'u']:
        count += 1
        continue
    print(i)  # printing characters except vowels
print("no of vowels in %s is %d" % (str, count))
