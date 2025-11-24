""
"""
OOPS Continue

Instance Methods: Methods are called using objects. 
Syntax to call the method:
obj_name.method_name(arguments)

Static Methods: Are methods which are called using class name. The methods
we used outside class were static methods
Syntax to call the method:
class_name.method_name

Generally static methods are called functions, but not a rule. And instance
methods are called methods.

Syntax to create static methods: We will @staticmethod decorator before function
name

@staticmethod
def func1(arguments):
    set of statements
    





"""
# class C1:
#     @staticmethod
#     def func1(a,b,c):
#         print(a,b,c)
#
# C1.func1(5,7,9)



# #New Program
# def func1(a,b,c):
#     print(a,b,c)
# class C1:
#     pass
# ob=C1()
# func1(ob,5,7)


# #New Program
# class C1:
#     def method1(self,ob1,ob2):
#         print(self,ob1,ob2)
#
# a1=C1()
# a2=C1()
# a3=C1()
# a1.method1(a2,a3)
# print(a1,a2,a3)

# #New Program
# L1=[]
# print(id(L1))
# L2=[]
# print(id(L2))
# L3=[]
# print(id(L3))
# a=5
# b=5
# print(id(a),id(b))

# #New Program
# class C1:
#     def __init__(self,n1,n2):   #Parameterized Constructor
#         self.a=n1
#         self.b=n2
#
# ob=C1(5,7)     #ob=self, n1=5,n2=7
# print(ob.a,ob.b)


# #New Program
# class C1:
#     def __init__(self,n1=1,n2=2):   #Parameterized Constructor
#         self.a=n1
#         self.b=n2
#
# ob=C1(7)     #ob=self, n1=5,n2=7
# print(ob.a,ob.b)

# #New Program
# class Customer():
#     def __init__(self,id=None,name=None,age=None,mob=None,city="Delhi"):
#         self.id=id
#         self.name=name
#         self.age=age
#         self.mob=mob
#         self.city=city
# id=input("Enter Cust ID:")
# name=input("Enter Cust ID:")
# age=input("Enter Cust ID:")
# cus=Customer(id,name,age)       #cus=Customer(name=name)
# print(cus.id,cus.name,cus.age,cus.mob,cus.city)

#New Program



"""
Abstraction: Hiding the code and variables from user. Hiding the information.


Encapsulation: Terms retrieved from capsule, like we store the medicine in 
capsule. Storing and associating the data/variables/methods with single object.

Inheritance: Accessing the Parent Property from the child class.
Why Inheritance: To make the code reusable

Polymorphism: Poly means many, morph means forms. 
Polymorphism: Many Forms: Same function names in different forms
Same function name with same or different signature in same or different class
signature means parameters/arguments
Polymorphism is of two types.
1. Overloading: Same function name, with different signature in same class.
Python doesn't support function overloading. Why?
In Python functions are also objects of function class. When we try to create
a new function in same class with same name then new function object is created
and it is assigned a new address, so previous function object is collected by
garbage collector ie deleted. (In Python whenever we crate any new object with
same name then previous object is deleted by garbage collector)


2. Overriding: Same function name with same signatures in derived(child) class.
In case of overriding, if we are calling the method through object of child class
then priority will be given to child class method.
 


Parent Class/Super Class/Base Class
Child Class/Sub Class/Derived Class

"""
# #New Program
# class C1:
#     def func1(self,a,b):
#         print(a,b)
#     def func1(self,a,b,c,d):
#         print(a,b,c,d)
# ob1=C1()
# ob1.func1(5,7)

# #New Program
# L1=["ab","cd"]
# L1.upper()      #AttributeError: 'list' object has no attribute 'upper'
# print(L1)


# #New Program
# class C1:
#     def method1(self):
#         print("I am in C1 Class")
#
# class C2:
#     pass
# ob=C2()
# ob.method1()        #AttributeError: 'C2' object has no attribute 'method1'



# #New Program
# class C1:
#     def method1(self):
#         print("I am in C1 Class")
#
# class C2(C1):       #C1 will become parent or super class of C2
#     pass
# ob=C2()
# ob.method1()


# #New Program
# class C1:
#     def method1(self):
#         print("I am in C1 Class")
#
# class C2(C1):       #C1 will become parent or super class of C2
#     def method1(self):
#         print("I am in C2 Class")
# ob=C2()
# ob.method1()


# #New Program
# class C1:
#     def __init__(self):
#         self.a=1
#         self.b=2
#     def showData(self):
#         print("I m in Class C1")
# class C2(C1):
#     pass
# ob=C2()
# ob.showData()
# print(ob.a,ob.b)

# #New Program
# class C1:
#     def __init__(self):
#         self.a=1
#         self.b=2
#     def showData(self):
#         print("I m in Class C1")
# class C2(C1):
#     def __init__(self):
#         self.c=3
#         self.d=4
#         super().__init__()
# ob=C2()     #Constructor
# ob.showData()
# print(ob.a,ob.b,ob.c,ob.d)  #AttributeError: 'C2' object has no attribute 'a'

# #New Program
# a=5
# print(a==5)
# if(a==5):
#     print("Hello")

"""In Python, all non zero, non None, non False values are considered as True Value"""

# #New Program
# if(1):
#     print("CETPA")
# if("Hello"):
#     print("CETPA")

# #New Program
# while(1):
#     print("CETPA")


#New Program
import requests
from pprint import pprint