str = "From Stephen.marquard@uct.ac.za Sat Jan 5 09: 14: 16 2008"
startIndex = str.find('@')
print(startIndex)
endIndex = str.find(' ', startIndex)
print(endIndex)
subString = str[startIndex+1:endIndex]
print(subString)
