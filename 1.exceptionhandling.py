
try:
    faren = float(input("Enter farenheit temperature:\n"))
    degree = (faren-32.0)*5/9.0
    l1 = [1, 2, 3, 4, 5]
    print(degree, "degree")
    l1[5] = 6
except IndexError:
    print("Index out of bound error")
except ValueError:
    print("Value error! Please Enter number\n")
else:
    print("No Exception")
finally:
    print("finally block")
