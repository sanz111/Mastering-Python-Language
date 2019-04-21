file1 = open("input.txt","r");
file2 = open("output.txt","w");

# #method1 using open() only
# sum = 0;
# mul = 0;
# sub = 0;
# for line in file1:
#     sum = sum+int(line);
#     mul = mul*int(line);
#     sub = sub-int(line);
#
# file2.write(str(sum)+"\n"+str(mul)+"\n"+str(sub)+"\n");

a,b = file1.read().rsplit(); #rsplit() and split() are same without aurguments
a = int(a);
b = int(b);

file2.write(str(a+b)+"\n"+str(a*b)+"\n"+str(a-b)+"\n");


