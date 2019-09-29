print("Printing numbers other than multiple of 5:\n")
inp = int(input("Enter Your top range: "))
while(inp >= 1):
    if(inp % 5 == 0):
        inp = inp - 1
        continue
    print(inp)
    inp = inp - 1
