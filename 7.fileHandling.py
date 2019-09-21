fileName = input("Enter the name of the file to be used\n")

try:
    file = open(fileName, "r+")  # reads the content line by line
    for line in file:
        if line.startswith("YOU"):
            # removes extra new line character from line
            print(line.rstrip())
            print("------------------------------------\nprinting each word of the line")
            words = line.split()
            for word in words:
                print(word)
except:
    print("Couldn't open file for writing")
    exit()

line = input("Enter the content to be written into the file:\n")
file.write("\n"+line+"\n")


# 2nd way of reading, recommended only when file is smaller in size than RAM
# reader=file.read()
# print(reader)
