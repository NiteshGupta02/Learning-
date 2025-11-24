"Python"
"""
Functions:

def <function_name>(Parameters):
    Indented Block of Statements
    return value..(Optional)
How to call the function:
function_name(arguments)

Indentation: is used to separate the block of statements
All the statements in a block will be at a fixed space from its
heading which is called indented statements.
Examples of headings are : function, loop, if, elif, class...
Headings are ended with colon: 

"""
# def func1():
#     print("Welcome to CETPA")
#     print("Hello World")
#
# print("I am out of Function")
# def func2():
#     print("This is another function")
# print("Main")
# #Only 2 print statements will run

#New Program
# print()

# New Program
# print("CETPA")

# #New Program
# def func1():
#     print("Welcome to CETPA")
#     print("Hello World")
# def func2():
#     print("This is another function")
#
# print("Main Started")
# func2()     #Calling of Funciton
# func2()     #Calling of Funciton
# func1()

# #New Program
# a,b=5,7
# s=a+b
# print(s)

# #New Program
# func1() #Error, function should be defined before calling
# def func1():
#     print("This is Function")

"""
Layers:
    PL: To interact with user
    BLL: To write the business logic
"""
# #New Program
# s=input("Enter Your Name:")
# res=len(s)
# print(len(s))
# print(res)

"""Whenever we create a new project or a new python file,
then few predefined files (libraries,packages,frameworks)
are automatically added in your program like builtins.py 
package

But for rest of the packages, you firstly need to add that
package in your program
Basic Syntax to add: import package_name

Once you imported the package, after that to use some
particular function of that package,
The syntax is
package_name.function_name(arguments)
"""

# #New Program
# #PL
# import operator
# import math
# no1=int(input("Enter First No:"))   #no1=5
# no2=int(input("Enter Second No:"))  #no2=7
# res=operator.add(no1,no2)   #res=no1+no2
# print("The sum of numbers is:",res)
# print("Factorial of First No:",math.factorial(no1))
# print("Factorial of Second No:",math.factorial(no2))

#New Program
  # print("CETPA")  #Error

# #Addition of 2 numbers
# #BLL
# def sum(a,b):       #Functions to add 2 numbers
#     s=a+b
#     return s
#
# #PL
# no1=int(input("Enter First No:"))   #no1=5
# no2=int(input("Enter Second No:"))  #no2=7
# res=sum(no1,no2)
# print("The sum of numbers is:",res)

# #New Program
# def len():
#     print("CETPA")
# len()

# #New Program
# import Prog5
# Prog5.func1()

# #New Program
# def myfunc(a,b):
#     print(a,b)
#
# myfunc(5,7)
# myfunc(5,7)
# myfunc(5,7)

# #New Program
# def add(a,b):
#     print(a+b)  #Not a good way
#
# a,b=5,7
# add(a,b)

# #New Program
# def add(a,b):
#     return a+b
#
# a,b=5,7
# s=add(a,b)
# print(s)
# print(add(a,b))

# #New Program
# #BLL
# def add(n1,n2):
#     r=n1+n2
#     return r
#
# #PL
# no1=int(input("Enter First No:"))
# no2=int(input("Enter Second No:"))
# res=add(no1,no2)
# print("Result is:",res)

"""
Each heading should have at least 1 statement inside it
If we don't have any statement then we can write pass 
"""

# #New Program
# def oddeven():
#     pass

# #New Program
# def func1():
#     print("CETPA")
# func1()

# #New Program
# def func1():print("CETPA")
# func1()

# #New Program
# #BLL
# def checkOdd(n):
#     rem=n%2     #n=5, rem=1
#     res=rem==1
#     return res  #return rem==1
#
# #PL
# no=int(input("Enter the number:"))  #5
# r=checkOdd(no)
# print("Whether the entered no is Odd? ", r)

"""
Private and Public Variables

All variables inside function are private variables ie 
these variables can be accessed only inside functions

Variables defined inside functions are global variables ie
they can be accessed inside functions directly still most
of time we avoid using it as it reduces the reusability of 
code

Parameters vs Arguments:
Parameters: The variables created at the time of function 
            definition/creation
Arguments: The values passed at the time of function calling

Parameters names and Arguments names can be same or different.
But parameters and arguments are different variables
ie The scope of parameters is only inside functions ie
parameters are local variables
"""
# def func1():
#     a=5
#
# func1()
# print(a)    #NameError: name 'a' is not defined

# #New Program
# def func1():
#     print(a)
# a=5
# func1()

# #New Program
# def add():
#     r=a+b
#     return r
# a,b=5,7
# m,n=2,3
# print(add())

# #New Program
# def add(c,d):
#     r=c+d
#     return r
# a,b=5,7
# m,n=2,3
# print(add(a,b))
# print(add(m,n))


# #New Program
# def add(a,b):
#     r=a+b
#     return r
#
# a,b=5,7
# r=add(a,b)
# print(r)

"""Inside functions if we have local variables with same name
as global variables then inside functions, preference is given
to local variables. Outside functions local variables can't be
accessed, means global variables will be accessed

Global variables can be accessed inside functions but can't
be modified inside functions directly, if we try to modify them
ie if we try to assign a new value to a global variable in
python then a new local variable will be created, why because
in Python variables are created by assigning the value to them
and inside function if we are creating any variable then these
are local variables.

Still if we want to modify global variables inside functions
and don't want to create local variables then we can use
global keyword
"""


# #New Program
# def func1():
#     print(a)
#
# a=5
# func1()

# #New Program
# def func1():
#     a=5
#
# func1()
# print(a)  #NameError

# #New Program
# def func1():
#     a=5
#     print(a)
#
# a=7
# func1()
# print(a)

# #New Program
# a=a+1
# print(a) #Error

# #New Program
# def func1():
#     a=a+1       #Error
#     print(a)
#
# a=5
# func1()

# #New Program
# def func1():
#     global a
#     a=5
#     print(a)
#
# a=7
# func1()
# print(a)
