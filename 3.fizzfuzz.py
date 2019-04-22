def check(i):
    if (inp % 3 == 0 and inp % 5 == 0):
        print("fizzfuzz")
    elif (inp % 3 == 0):
        print("fizz")
    elif (inp % 5 == 0):
        print("fuzz")
    else:
        print(inp)


inp = int(input("Enter any integer value to play fizzfuzz: "))
for i in range(inp):
    check(i)
