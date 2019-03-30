#!/usr/bin/python3

try:
    fhandle = open("myfile.txt","w")
    fhandle.write("This is the data being written to the file")

except IOError as e:
    print("Failed! Unable to write to the file",e)
except Exception as e:
    print("Error other than IOError has occured")
else:
    print("Data written to the file succesfully")
    fhandle.close();