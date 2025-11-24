""
""""""
# def addCustomer(id,name,age,mob):
#     idlist.append(id)
#     namelist.append(name)
#     agelist.append(age)
#     moblist.append(mob)
# def searchCustomer(id):
#     index=idlist.index(id)
#     return index
# def deleteCustomer(id):
#     index=idlist.index(id)
#     idlist.pop(index)
#     namelist.pop(index)
#     agelist.pop(index)
#     moblist.pop(index)
# def modifyCustomer(id,name,age,mob):
#     index=idlist.index(id)
#     namelist[index]=name
#     agelist[index]=age
#     moblist[index]=mob
#
#
# print("welcome to chintu CMS")
#
# idlist=[]
# namelist=[]
# agelist=[]
# moblist=[]
# def showCustomer(i):
#     print("Customer ID:",idlist[i],"Customer Name:",namelist[i],"Customer Age:",agelist[i],"Customer Mob:",moblist[i],)
# while 1 :
#     c=input('''
#              enter choice :
#           1.Add customer :
#           2.Search customer :
#           3.delete customer :
#           4.Modify customer :
#           5.Display all :
#           6.Exit.
#           ''')
#
#     if c=="1" :
#      id = int(input("enter customer id :"))
#      name = input("enter customer name :")
#      age = input("enter customer age :")
#      mob = input("enter customer mob no. :")
#      addCustomer(id,name,age,mob)
#      print("customer added succesfully")
#     elif c=="2" :
#      id = int(input("enter the customer id you want to search :"))
#      i = searchCustomer(id)
#      showCustomer(i)
#     elif c=="3" :
#      id = int(input("enter customer id you want to delete :"))
#      id=deleteCustomer(id)
#      print(id)
#      print("customer deleted ")
#     elif c=="4":
#         id =int(input("enter customer id you want to modify :"))
#         name=input("Enter Customer Updated Name:")
#         age=input("Enter Customer Updated Age:")
#         mob=input("Enter Customer Updated Mob:")
#         modifyCustomer(id,name,age,mob)
#         print("Customer Modified.")
#     elif c=="5" :
#         for i in range(len(idlist)):
#             showCustomer(i)
#     elif c=="6" :
#      print("thanks for using my cms.")
#      break

"""
Different Types of Functions / Different Argument types in functions
Total 5 Types of Arguments are there
1. Positional Arguments/Required Arguments: When we call these functions
then we should follow the correct position and correct no of arguments
2. Keyword Argument Functions: No of arguments are fixed but position can
be changed
3. Default Argument Functions: No of arguments are not fixed but position is
fixed, we can pass less than arguments given in formal parameters
Mixed Argument: Above 3 can be mixed together 
4. Variable Length Argument: tuple based:
5. Variable Length Argument: dict based: (Keyword Variable Length Argument) 

"""
# #New Program
# def add(a,b):     #a,b Parameters or Formal Parameters
#     return a+b
#
# print(add(2,3))   #2,3 Argument or Actual Parameter

# #New Program
# def add(a,b):
#     return a+b
#
# print(add(2,3,4))  #Error

# #New Program
# def sub(a,b):       #a,b Required Argument Function
#     return a-b
#
# c,d=6,4
# r=sub(d,c)
# print("Result of c-d is:",r)    #Result of d-c rather c-d

# #New Program
# def sub(a,b):       #a,b Required Argument Function
#     return a-b
#
# c,d=6,4
# r=sub(b=d,a=c)
# print("Result of c-d is:",r)    #Result of d-c rather c-d


# #New Program
# cusdict={}
# def addCustomer(id,name,age,mob,email):
#     cusdict[id]=[name,age,mob,email]
#     print(cusdict)
#
# addCustomer(10,39,"Vikas",1234,"a@b.com")   #Required argument
# addCustomer(id=20,email="abc@gmail.com",age=41,mob=2345,name="Anil")

# #New Program
# def add(a=1,b=2,c=3):   #Default Argument Functions, add(a,b,c)
#     print(a+b+c)
#
# add()   #
# add(3)  #a=3
# add(3,4)    #a=3,b=4
# add(3,4,5)  #a=3,b=4,c=5

# #New Program
# L1=[2,3,4,7,6,4]
# L1.sort()
# print(L1)
# L1.sort(reverse=True)   #reverse is default argument
# print(L1)

# #New Program
# def add(a,b=2,c=3):     #def add(a,b,c).......add()
#     print(a+b+c)
#
# # add()   #Error
# add(2)      #a=2

# #New Program
# def add(a,b=2,c=3):     #def add(a,b,c).......add()
#     print(a+b+c)
#
# # add()   #Error
# add(2,4)      #a=2,b=4

# #New Program
# def add(a,b=2,c=3):     #def add(a,b,c).......add()
#     print(a+b+c)
#
# # add()   #Error
# add(c=9,a=2)      #a=2,b=4


# #New Program
# def add(a,b=2,c=3):     #def add(a,b,c).......add()
#     print(a+b+c)
#
#
# add(c=9,b=2,5)      #Error SyntaxError: positional argument follows keyword argument


# #New Program
# print("CETPA",end="*")

# #New Program
# print(end="*","CETPA")  #SyntaxError: positional argument follows keyword argument

# #New Program
# def add(t1):        #t1=(2,3,4,5)
#     r=0
#     for e in t1:
#         r=r+e
#     return r
#
# t1=(2,3,4,5)
# r=add(t1)
# print("Sum of Tuple Elements:",r)


# "Variable length argument: tuple"
# def func1(*t):
#     print(t)
#
# func1()
# func1(2,3,4)
# func1(2,3,4,5,6,7,8,9)

# #New Program
# def add(*t):    #t=(2,3)
#     r=0
#     for e in t:
#         r=r+e
#     print(r)
#
# add(2,3)
# add(2,3,4,5)
# add(2,3,4,5,6,7,8)
# add()

"""Python recommends to use formal parameter names as *args for variable 
length argument functions and **kwargs for variable length keyword argument 
function 
"""
# #New Program
# def add(*args):    #args=(2,3)
#     r=0
#     for e in args:
#         r=r+e
#     print(r)
# add(2,3)
# add(2,3,4,5)
# add(2,3,4,5,6,7,8)
# add()



"""No Practise No Learning"""

#New Program
"""
5. Variable Length Argument: dict based: (Keyword Variable Length Argument)

"""
# def func1(**d):
#     print(d)
#
# func1(a=1,b=2,c=3)
# func1(a=1,b=2,c=3,d=4,e=5,f=6)
# func1()

# #New Program
# def add(**kwargs):      #kwargs={'a':2,'b':3}
#     r=0
#     for e in kwargs.values():
#         r=r+e
#     print(r)
# add(a=1,b=2,c=3)
# add(a=1,b=2,c=3,d=4,e=5,f=6)
# add()


# #New Program
# d1={'id':None,'age':None,'name':None,'mob':None,'email':None}
# def addCustomer(**kwargs):
#     print(kwargs)
#     d1.update(kwargs)
#     print(d1)
#
# addCustomer(age=39,name="Vikas",email="vikaskalra@cetpainfotech.com")

"""
Easy In Easy Out : Industry

Difficult In Difficult Out: Industry

"""

"""
Module: Are the Python files: 

Module/Package/Library/Framework
3 Types
1. builtin modules: Files already installed in our system and can be accessed
directly in our program without adding them 
2. inbuilt modules: Files already installed in our system and can't be accessed
directly in our program. To use them, we firstly need to add them in our program
3. external modules: Should install seperatly from internet and then use them


"""
# s="CETPA"
# print(len(s)) #print and len functions are written in builtin modules


# #New Program
# import math     #math inbuilt module
# a,b=1000,10
# print(math.log(a,b))

# #New Program
# import random
# print(random.random())

# #New Program
# import random
# idlist=[]
# while(1):
#     r=random.randint(1,10000)
#     if(r not in idlist):
#         idlist.append(r)
#         break
# print(idlist)

# #New Program
# import Module1
# r1=Module1.add(5,7)
# r2=Module1.sub(3,4)
# r3=Module1.m*Module1.n
# print(r1,r2,r3)





