# # addition of two numbers
# a=input("enter first number: ")
# a=int(a)
# b=input("enter second number: ")
# b=int(b)
# print("the additon of a nd b is ",a+b)
''' f=open("pogo.txt","w")#creating a file
f.write("\nMachine Learnig ")#write to a file
 f.write("\n Internet of things\n")
 f=open("pogo.txt","r+")
 a=f.readline()
 print(a)
 f.close() '''
''' find the size of the file.
def file_size(file):
    import os
    statinfo = os.stat(file)
    return statinfo.st_size
print("file size in byest of plain file=",file_size("pogo.txt"),"bytes") '''


