def factorial(n):
    num = 1
    while(n >= 1):
        num = num*n
        n = n-1
    return num


inp = int(input("Find factorial of: "))
print(factorial(inp))
