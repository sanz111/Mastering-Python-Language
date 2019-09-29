string = "Cisco Switch"
print ("Remember string in python is: An array of characters with index 0 from LHS and -1 from RHS")
print ("Example 1: string = \"Cisco Switch\"\n-------------------------------------")
print ("string[0] = " + string[0] + " and string[-1] = " +string[-1])
print ("string.index(\"i\") = ", (string.index("i")) )
print ("string.count(\"i\") = ", (string.count("i")))
print ("string.find(\"co\") = ", (string.find("sco")))
print ("string.lower() = " + string.lower())
print ("string.upper() = " + string.upper())
print ("string.startswith(\"C\") = ", string.startswith("C"))
print ("string.endswith(\"L\") = ", string.endswith("L"))
print ("\"_\".join(string) = ", "_".join(string))
print ("----------------------------------------------------------")

string = "apple,ball,cat"
print ("Example 2: string = \"apple,ball,cat\"")
print (len(string))
print ("string.split(\",\") = ",  (string.split(",")))
print ("------------------------------------------------")

string = "$$$Cisco Switch$$$"
print ("Example 3: string = \"$$$Cisco Switch$$$\"\n------------------------------")
print ("string.strip(\"$\") = " + string.strip("$"))
print ("string.replace(\"C\",\"D\") = " + string.replace("C","D"))

print ("Odd number using range:", (range(1,10,2)))

for letter in string:
    print(letter[0] * 5)
else:
    print("string array has finished")


x = "Cisco"
if "i" in x:
    print(x)
    print()


