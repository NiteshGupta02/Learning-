""
"""
OOPS: 

Data Types
Single Element/Single Valued/Single Variable:
int
float
complex
bool
NoneType

Multi Element/Multi Valued/Multi Variable/Iterators
str
list
tuple
dict
set
frozenset
user defined data type: Collection of heterogeneous data type

mutable: list, dict, set and user defined data type

There is no negative marking in our class: 
"""
# def func1(L2):      #L2 address 1000
#     L2.append(5)    #L2 address 1000
#
# L1=[2,3,4]      #L1 base address 1000
# func1(L1)       #L2=L1,
# print(L1)

# #New Program
# a,b,c,d=2,3.5,False,"CETPA"
# print(id(a))
# L1=[a,b,c,d]
# print(L1)
# print(id(L1[0]))

# #New Program
# def method1(self):  #self=[2,3,4]
#     self[0]=10      #self=[10,3,4]
#
# L1=[2,3,4]
# method1(L1)     #self=L1
# print(L1)

# #New Program
# L1=[2,3,4]
# L1.append(5)    #object_name.method_name(arguments)
# print(L1)

"""In Python all variables are of reference type. When we print few 
variables then their values are printed while on the other hand for
other variables their address is printed

When we print objects of user defined data type (user defined class) then
their address will be printed

Object of any user defined or predefined class
ob_name=class_name()
"""

# #New Program
# L1=list()
# print(L1)
# print(type(L1))

# #New Program
# class C1:
#     def method1(a,b):
#         print(a,b)
#
# ob1=C1()    #ob1=1000, formal = actual, a=ob1,b=5
# m=5
# ob1.method1(m)

# #New Program
# class C1:
#     def method1(self,b):
#         print(self,b)
#
# ob1=C1()    #ob1=1000, formal = actual, a=ob1,b=5
# m=5
# print(ob1)
# ob1.method1(m)

"""Whenever we create an object in python of some class then
constructor of that class is automatically called 
"""

# #New Program
# L1=[]
# L2=[]
# L1.append(5)
# print(L1,L2)

# #New Program
# class C1:
#     def __init__(self):
#         self.a=5
#         self.b=7
#
# ob1=C1()    #ob1 is of C1 type,


# #New Program
# class C1:
#     pass
#
# ob1=C1()
# ob2=C1()
# ob1.a=5
# ob1.b=7
# print(ob1,ob2)
# print(ob1.a)
# print(ob2.a)

# #New Program
# class C1:
#     def __init__(self):
#         self.a=5
#         self.b=7
# ob1=C1()        #self=ob1
# ob2=C1()        #self=ob1
# print(ob1.a,ob1.b)
# print(ob2.a,ob2.b)

# #New Program
# def func1(L):       #L address 1000, L=[]
#     L.append(5)     #L=[5], L address 1000
# def func2(L):       #L=[5], L address 1000
#     L[0]=7          #L=[7], L address 1000
#
# L1=[]       #L1 address 1000
# func1(L1)   #formal=actual, L=L1
# print(L1)   #[5]
# func2(L1)   #L=L1
# print(L1)   #[7]



# #New Program
# class C1:
#     def __init__(self): #self=1000, 1000.a=5, self.a=5
#         self.a=5
#     def method1(self):  #self=1000, self.a=5
#         self.a=7
#
# ob1=C1()        #ob1 address 1000, ob1.a=5
# ob1.method1()   #ob1.a=7
# print(ob1.a)

"""
CRUD: Create Read Update Delete
CMS: Add Customer, Search Customer, Modify Customer, Delete Customer


Possible Classes for Amazon:


Product
Customer
Seller
Cart.
.
.

"""

# #New Program: Addition of 2 Numbers using OOPS:
# #BLL
# class Calci:
#     def __init__(self):
#         self.a=0
#         self.b=0
#         self.r=0
#     def add(self):  #self=1000, self.a=5, self.b=7,self.r=0
#         self.r=self.a+self.b    #self.r=12
# #PL
# ob1=Calci()     #ob1.a=0,ob1.b=0,ob1.r=0, ob1=1000
# ob1.a=int(input("Enter First No:")) #ob1.a=5, ob1=1000
# ob1.b=int(input("Enter Second No:")) #ob1.b=7, ob1=1000
# ob1.add()
# print("Result:",ob1.r)


"""Calculator
"""
# import math
# class Calci:
#     def __init__(self):
#         self.no1=0
#         self.no2 = 0
#         self.res = 0
#     def add(self):      #self=1000,self.no1=5, self.no2=7, self.res=0
#         self.res=self.no1+self.no2  #self.res=12
#     def sub(self):      #self=1000,self.no1=5, self.no2=7, self.res=0
#         self.res=self.no1-self.no2  #self.res=12
#
# while(1):
#     cal=Calci()     #cal.no1=0,cal.no2=0,cal.res=0, cal 1000
#     ch=input("Enter Choice +, -, *, /, log:")
#     cal.no1=int(input("Enter First No:"))       #cal.no1=5
#     cal.no2 = int(input("Enter Second No:"))    #cal.no2=7
#     if(ch=="+"):
#         cal.add()       #cal.res=12
#         print("Result:",cal.res)
#     elif (ch == "-"):
#         cal.sub()
#         print("Result:", cal.res)
#     elif (ch == "log"):
#         cal.res=math.log(cal.no1,cal.no2)
#         print("Result:", cal.res)

"""
We have two types of variables and two types of methods in class ie
static variable/class variable
instance variable/object variable

instance variable/object variable are different variables for different objects.
instance variable are accessed through object name.

static variable/class variable are same variables for different objects. class
variables are accessed through class name
We can access static variables through object name also but preferably we
should access it through class name only, because if we try to modify static
variables through object name then new instance variables will be created. 
class variables can be modified only through class name

static method/class method
instance method/object method

How to create static variable
Directly create a variable inside class.  

All variables we studied till now outside class, all were static variables
"""
# class C1:
#     m=1         #Static Varaible
#     def __init__(self):
#         self.a=2    #Instance Variable/object variable
#         self.b=3    #Instance Variable/obejct variable
#
# print(C1.m)
# ob1=C1()
# print(ob1.a,ob1.b)
# ob2=C1()
# print(ob2.a,ob2.b)

#New Program
# class C1:
#     m=1         #Static Varaible
#     def __init__(self):
#         self.a=2    #Instance Variable/object variable
#         self.b=3    #Instance Variable/obejct variable
#
# print(C1.m)
# C1.m=5
# ob1=C1()
# print(ob1.a,ob1.b,ob1.m)
# ob2=C1()
# print(ob2.a,ob2.b,ob2.m)
# ob1.m=7         #Here a new object variable with ob1 object will be created
# print(ob1.m,ob2.m,C1.m)

"""Customer Management System using OOPS
Assignment: With 10 varaibles
"""
class Customer:
    cuslist=[]      #Static Variable
    def __init__(self): #self=1000
        self.id=0
        self.name = 0
        self.age=0
        self.mob = 0
    def addCustomer(self):  #self=1000, self=2000
        Customer.cuslist.append(self)       #cuslist=[1000,2000,3000....
    def searchCustomer(self):   #self=9000, self.id=20, self.name=0....
        for e in Customer.cuslist:  #e=1000
            if(e.id==self.id):
                self.name=e.name    #self.name="Anil"
                self.age=e.age      #self.age=41
                self.mob=e.mob
                break       #return
    def deleteCustomer(self):   #self=10000, self.id=30
        # for e in Customer.cuslist:
        #     if(e.id==self.id):
        #         Customer.cuslist.remove(e)
        #Another Way
        for i in range(len(Customer.cuslist)):      #i=0,1,2
            if(self.id==Customer.cuslist[i].id):
                Customer.cuslist.pop(i)
                return
    @staticmethod
    def deleteCustomerStatic(id):
        for i in range(len(Customer.cuslist)):      #i=0,1,2
            if(id==Customer.cuslist[i].id):
                Customer.cuslist.pop(i)
                return

    def modifyCustomer(self):       #self=11000, self.id=20,self.name="Banti"...
        for e in Customer.cuslist:  #e=1000
            if(e.id==self.id):
                e.name=self.name
                e.age=self.age
                e.mob=self.mob




print("Welcome to Rahul's CMS")
def showCustomer(e):        #e=1000
    print("Cust ID:",e.id,"Cust Name:",e.name,"Cust Age:",e.age,"Cust Mob:",e.mob)
while(1):
    cus=Customer() #cus=1000, 4 instance variables will be created, cus=9000
    choice=input("Enter Choice: 1 Add Cust, 2 Search, 3 Delete, 4 Modify, 5 Display All, 6 Exit:")
    if(choice=="1"):    #Add Customer
        cus.id=input("Enter Customer Id:")          #cus.id=10
        cus.name=input("Enter Customer Name:")      #cus.name="vikas"
        cus.age=input("Enter Customer Age:")        #cus.age=39
        cus.mob=input("Enter Customer Mob:")        #cus.mob=123
        cus.addCustomer()
    elif(choice=="5"):  #Display All
        for e in Customer.cuslist:  #e=1000
            showCustomer(e)
    elif(choice=="2"):   #Search Cust, cus address 9000, cus.id=0,cus.name=0,cus.age=0,cus.mob=0
        cus.id=input("Enter Cust ID:")  #cus.id=20, 9000.id=20
        cus.searchCustomer()
        showCustomer(cus)
    elif(choice=="3"):   #Delete Cust, cus=10000
        # cus.id=input("Enter Cust ID:")  #cus.id=30, 10000.id=30, 10000.name=0.....
        # cus.deleteCustomer()    #cus=10000
        id=input("Enter Customer ID:")
        Customer.deleteCustomerStatic(id)
        print("Customer Deleted Successfully")
    elif(choice=="4"):  #Modify Cust, cus=11000, cus.id=0,cus.name=0....
        cus.id=input("Enter Cust Id to Modify Cust:")   #cus.id=20
        cus.name=input("Enter Cust Updated Name:")      #cus.name="Banti"
        cus.age = input("Enter Cust Updated Age:")      #cus.age=42
        cus.mob = input("Enter Cust Updated Mob:")      #cus.mob=9212468020
        cus.modifyCustomer()
        print("Customer Modified Successfully")
    elif(choice=="6"):
        print("Thanks for using Rahul's CMS")
        break
    else:
        print("Incorrect Choice")


"""Assignment: Create CMS using 10 Variables and make some changes like
add some checks like age,mob nos in correct format and so on..

"""


