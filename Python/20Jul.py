""
"""
OOPS: Object Oriented Programming

Class: Is a data type or a user defined data type.
Class is a collection of Variables and Methods (Functions)

Syntax:
class Class_Name:
    Collection of Methods and Variables ie properties or attributes

How to create an object of a class: 
Syntax:
ob_name=Class_Name(Arguments)

"""
# #New Program
# x=int()
# print(x,type(x))
# x=list()
# print(x,type(x))

# #New Program
# class Vikas:
#     pass
# x=Vikas()
# print(x)
# print(type(x))

"""
How to call a function: 
function_name(arguments)

If we create a function inside class then generally we call it a method.
Syntax to call a function:
obj_name.method_name(arguments)

When we call a method using object name then object is also passed to method
and it is passed to the first argument of the method ie object is passed to
first formal parameter of method. Python recommends that the first parameter
name in formal where object will be received the name of this parameter should
be self (Its a Convention not a Rule).

In following program, 2 arguments are passed to append method ie L1 and 10.
L1 will be passed to self and 10 to next arguments defined in append method.
"""
#New Program
# L1=[2,3,4]
# L2=[4,5,6]
# L1.append(10)
# print(L1)
"Please Be Participative: No Negative Marking"


# #New Program
# s="CETPA INFOTECH"
# n=s.count("T")
# print(n)
# n=s.count("T",5,50)
# print(n)

"""All variables in Python are of ref type ie if we assign one variable to
another variable then address of RHS variable is assigned to LHS variable
As all variables in Python are of ref type so function calling in Python is 
based on 'Call by Reference Concept'

In any programming language when we call a function then actual parameters
are assigned to formal parameters

def func1(a,b):     #a and b are formal parameters
    print(id(a),id(b))

m,n=5,7
print(id(m),id(n))
func1(m,n)      #a=m,b=n,  m and n are actual parameters



"""

# #New Program
# class C1:
#     def method1(self,a,b):
#         print(a,b)
#         print(self)
#
# ob1=C1()    #ob1 type is C1, ob1 is an object of C1 class.
# print(ob1)
# ob1.method1(5,7)    #self=ob1, a=5,b=7
# #print(self)        #Error ie self is local varaible or object of the class

"""Class is a collection of variables and methods. The variables and methods
collectivly inside class are called attributes or properties
Class is a collection of attributes
Class is a collection of properties
"""
# #New Program
# class C1:
#     def showData1(self,a,b):
#         print(a,b)
#     def showData2(self,a,b):
#         print(a,b)
# class C2:
#     def method1(self,a,b):
#         print(a,b)
# ob1=C2()
# m,n=5,7
# ob1.showData1(m,n)  #AttributeError: 'C2' object has no attribute 'showData1'

# #New Program
# L1=["ab","cd"]
# L1.upper()   #AttributeError: 'list' object has no attribute 'upper'
# print(L1)

"""
CMS: New Customer
id=input("Enter Customer ID:")
name=input("Enter Customer Name:")
age=input("Enter Customer Age:")
mob=input("Enter Customer Mob:")

How to define variables inside class


"""
# #New Program
# def func1():
#     print("CETPA")
# func1=5
# func1() #Error: TypeError: 'int' object is not callable

# #New Program
# idlist=[]
# namelist=[]
# id1=10
# name="Vikas"
# print(id(id1))
# print(id(name))
# idlist.append(id1)
# namelist.append(name)
# print(idlist,namelist)
# print(id(idlist[0]),id(namelist[0]))

"""
__init__ is a method inside class which is called a constructor. Whenever
we create the object of the class then __init__ method is automatically called
"""

# #New Program
# class C1:
#     def __init__(self):
#         print("CETPA")
#
# ob1=C1()
# ob2=C1()

"""Class is a collection of variables and method. Now what we want, once we
create an object of a Customer class then automatically the 4 variables of
that particular customer should be created

Variables inside class
Standard Syntax to create the variable of an object of some class
object_name.variable_name=variable_value

Inside class object name is self
Syntax to create a variable inside class
self.var_name=var_value

Syntax to create a variable outside class for some particular object
obj_name.var_name=var_value

"""

# class Student:
#     def __init__(self):
#         self.id=0
#         self.name=""
#         self.age=0
#         self.mob=0
#
# stu1=Student()


#New Program
# class Customer:
#     pass
# ob1=Customer()
# ob2=Customer()
# ob1.id=0
# ob1.name=0
# ob1.age=0
# print(ob1.id,ob1.name,ob1.age)

"""In above program 3 variables will be created for ob1 but not for ob2"""
# class C1:
#     def createVariables(self):
#         self.id=0
#         self.age=0
#         self.name=0
#
# ob1=C1()
# ob1.createVariables()   #self=ob1
# print(ob1.id,ob1.name,ob1.age)
# ob2=C1()
# print(ob2.id,ob2.name,ob2.age)  #AttributeError: 'C1' object has no attribute 'id'

# #New Program
# class Customer:
#     def __init__(self):
#         self.id=0
#         self.name = 0
#         self.age = 0
#         self.mob = 0
# cus1=Customer() #   #self=cus1
# print(cus1.id,cus1.name,cus1.age,cus1.mob)
# cus2=Customer() #   #self=cus2
# print(cus2.id,cus2.name,cus2.age,cus2.mob)

# #New Program
# class Customer:
#     def __init__(self):
#         self.id=0
#         self.name = 0
#         self.age=0
#         self.mob=0
# cuslist=[]
# for i in range(3):
#     cus=Customer()  #cus=1000
#     cus.id=input("Enter Customer ID:")
#     cus.name = input("Enter Customer Name:")
#     cus.age=input("Enter Customer Age:")
#     cus.mob = input("Enter Customer Mob:")
#     cuslist.append(cus)
# print(cuslist)
# for e in cuslist:   #e=cus1
#     print("Cust ID:",e.id,"Cust Name:",e.name,"Cust Age:",e.age,"Cust Mob:",e.mob,)

# #New Program
# L1=[2,3,4]
# print(id(L1))
