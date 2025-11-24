""
"""
File Handling: How to read and write the data in computer files in hard disk
Modes:
Text Mode/String Mode/Character Modes:
    w: Write Mode: If file doesn't exist then a new file will be created, if
        file exists then it will be truncated first (data erase) and then our
        data will be written from the starting of the file.
    r: Read Mode: If file doesn't exist then error (FileNotFoundError) else
        data will be accessed from starting of file
    a: Append Mode: If file doesn't exist then a new file will be created, if
        file exists then data will be written at the end of the file
    w+: Write and Read Mode:
    r+: Read and Write Mode:
    a+: Append and Read Mode:

Binary Modes:
    wb: Write Binary
    rb: Read Binary
    ab:
    wb+:
    rb+:
    ab+:
f=open("D:/vikas/cetpa1.txt","w")
f will be the object of TextIOWrapper Class

Firstly to access methods used in File handling, we need to create an object
of TextIOWrapper class using open function

Syntax of open function
file_type_object=open("Path of the File",Mode_to_access_the_file)
"""
# #New Program
# f=open("D:/vikas/cetpa1.txt","w")
# print(type(f))


# #New Program
# f=open("D:/vikas/cetpa2.txt","w")
# data="""Welcome to CETPA.
# CETPA is an Award Winning Training Company.
# Vikas Sir is going to launch a new batch"
# """
# f.write(data)
# # f.close()

# #New Program
# f=open("D://vikas/cetpa2.txt","w")


# #New Program
# f=open("cetpa2.txt","w")
# f.write("CETPA Infotech")
# f.close()

# #New Program
# f=open("cetpa2.txt","w")
# L=["Welcome to CETPA","CETPA Infotech Pvt. Ltd.","Hello"]
# f.write(L)      #TypeError: write() argument must be str, not list
# f.close()

# New Program
# f=open("D://vikas/cetpa3.txt","w")
# L=["Welcome to CETPA","CETPA Infotech Pvt. Ltd.","Hello"]
# f.writelines(L)
# f.close()

# #New Program
# f=open("D://vikas/cetpa4.txt","w")
# L=["Welcome to CETPA\n","CETPA Infotech Pvt. Ltd.\n","Hello"]
# f.writelines(L)
# f.close()

# #New Program
# f=open("D://vikas/cetpa5.txt","r") #FileNotFoundError: [Errno 2] No such file or directory: 'D://vikas/cetpa5.txt'
# s=f.read()
# print(s)
# f.close()

# #New Program
# f=open("D://vikas/cetpa3.txt","r")
# s=f.read()
# print(s)
# f.close()

# #New Program
# import os
# os.startfile("D:\VK HP Laptop10Oct22\CETPA Videos\cetpa.mp4")

# #New Program
# f=open("D://vikas/cetpa4.txt","r")
# L=f.readlines()
# print(L)
# f.close()

# #New Program
# f=open("D://vikas/cetpa4.txt","r")
# L=f.readlines()
# print(L)
# for line in L:
#     print(line,end="")
# f.close()

# #New Program
# f=open("D://vikas/cetpa4.txt","a")
# f.write("Good Morning")
# f.close()

# #New Program
# d="Welcome to CETPA"
# print(type(d))
# print(d)
# d=b"Welcome to CETPA"
# print(type(d))
# print(d)

# #New Program
# f=open("D:/vikas/cetpa5.txt","wb")
# d=b"Welcome to CETPA"
# f.write(d)
# f.close()

# #New Program
# f=open("D:/vikas/cetpa4.txt","r")
# d=f.read(5)
# print(d)
# d=f.read(4)
# print(d)
# f.close()


# #New Program
# f1=open(r"D:\VK HP Laptop10Oct22\CETPA Videos\cetpa.mp4","rb")
# print(f1.read(1000))


# #New Program
# f1=open(r"D:\VK HP Laptop10Oct22\CETPA Videos\cetpa.mp4","rb")
# data=f1.read()
# f2=open(r"D:\vikas\cetpa1.mp4","wb")
# f2.write(data)
# f1.close()
# f2.close()

# #New Program
# f=open(r"D:\\vikas\cetpa4.txt","r")
# print(f.tell())
# print(f.read(4))
# print(f.tell())
# print(f.read(5))
# print(f.tell())
# f.close()

"""
seek method: To move the cursor to some particular position in file
Syntax:
seek(offset,whence)
offset: no of characters to move
whence: In txt mode: whence can have only value 0 which means we have to move
the cursor w.r.to starting of file
Default value of whence is 0 

whence in binary mode: 
whence: 0: wrto starting of file
whence: 1: wrto current cursor position
whence: 2: wrto end of file

"""

# #New Program
# f=open(r"D:\\vikas\cetpa4.txt","r")
# f.seek(5)
# d=f.read(4)
# print(d)
# f.close()

# #New Program
# f=open(r"D:\\vikas\cetpa3.txt","rb")
# f.seek(-5,2)
# d=f.read(4)
# print(d)
# f.close()

# #New Program
# f=open(r"D:\\vikas\cetpa3.txt","rb")
# d=f.read(4)
# print(d)
# f.seek(-2,1)
# d=f.read(4)
# print(d)
# f.close()

#New Program

