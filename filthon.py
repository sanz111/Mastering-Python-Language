fname = input("Enter the name of the file to be used\n")

try:
    file = open(fname, "a+")  # reads the content line by line
    for line in file:
        if line.startswith("you"):
            print(line.rstrip())  # removes new line character from line
        else:
            print("No line starts with YOU here, see the file content:\n")
            print(line)
except:
    print("Couldn't open file for writing")
    exit()

line = input("Enter the content to be written into the file:\n")
file.write("\n"+line+"\n")


# 2nd way of reading, recommended only when file is smaller in size than RAM
# reader=file.read()
# print(reader)
