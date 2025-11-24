""
"""
Python Continue
"""
"""We have 4 numbers. Add first 2 numbers, subtract next 2 numbers and multiply the result"""
# #BLL
# def add(a,b):
#     return a+b
# def sub(a,b):
#     return a-b
# def mul(a,b):
#     return a*b
# #Presentation Layer
# no1=int(input("Enter First No:"))
# no2=int(input("Enter Second No:"))
# no3=int(input("Enter Third No:"))
# no4=int(input("Enter Fourth No:"))
# r1=add(no1,no2)
# r2=sub(no3,no4)
# res=mul(r1,r2)
# print("Result:",res)

# #New Program
# #BLL
# def myfunc(a,b,c,d):
#     r1=a+b
#     r2=c-d
#     r=r1*r2
#     return r    #return (a+b)*(c-d)
# #PL
# no1=int(input("Enter First No:"))
# no2=int(input("Enter Second No:"))
# no3=int(input("Enter Third No:"))
# no4=int(input("Enter Fourth No:"))
# res=myfunc(no1,no2,no3,no4)
# print("Result:",res)


# #New Program
# "2.	Reverse a string input by user without using loops or methods."
# s="cetpa"
# print(s[::-1])


"""
Conditional Statements:
if, elif and else: These are keywords in Python and represents headings
headings: There should be some block of code inside it. Block of code will be
indented block of code.
we pass conditions in if and elif blocks and if the condition is True, we 
enter inside the block else we won't

So if we have one if and corresponding multiple elif statements in a program 
then at whatever heading, condition goes True, other conditions won't be checked
In One complete part of code:
We can have only if, 
We can have if and single or multiple elif
we can have single if and single else
we can have single if, single or multiple elif, and single else

Else in case we have one if and then we start another if at same indentation
level then it won't have any relation with previous if
"""
# a,b=5,7
# s=a+b
# print(s)

"""Comparison Operators: ==, <, >, <=, <=, !="""

# #New Program
# a,b=5,7
# x=1
# if(x==1):       #== is a comparison operator
#     print(a+b)
# else:
#     print(a-b)

# #New Program
# a,b=5,7
# x=1
# if(x==1):       #== is a comparison operator
#     print(a+b)
# else:
#     print(a-b)


# #New Program
# a,b=5,7
# x=input("Enter the Number between 1 to 4:")
# if(x=='1'):
#     s=a+b
#     print("Res:",s)
# elif(x=='2'):
#     s=a-b
#     print("Res:", s)
# elif(x=="3"):
#     s=a*b
#     print("Res:",s)
# elif(x=="4"):
#     s=a/b
#     print("Res:",s)
# else:
#     print("Incorrect Input")


# #New Program
# a,b=5,7
# x=10
# if(x==10):
#     print("CETPA")
# else:
#     print("ABC")
# if(x>=10):
#     print("Hello")
# if(x!=9):
#     print("Welcome")
#     print("Hi")


# #New Program
# #BLL
# def evenOdd(n):
#     if(n%2==0):
#         return "Even"
#     else:
#         return "Odd"
#
#
# #PL
# no=int(input("Enter Any Number:"))
# res=evenOdd(no)
# print("The Entered Number is:",res)

"""
Arithmetic Operators: Works on Numbers
+
-
*
/
%
**
//  : Floor Division : Floor Value After Division

"""


# #New Program
# a,b=-7,2
# print(a//b)
# a,b=7,2
# print(a//b)

# # #Mini Project: Scientific Calculator
# #BLL
# import operator
# import math
# def add(a,b):
#     return a+b
# def sub(a,b):
#     return a-b
# def div(a,b):
#     return a/b

# #PL
# no1=int(input("Enter First No:"))
# no2=int(input("Enter Second No:"))
# op=input("Enter Operation +, -, *, /, pow, log:")
# if(op=="+"):
#     res=add(no1,no2)
#     print("Result:",res)
# elif(op=="-"):
#     res=sub(no1,no2)
#     print("Result:",res)
# elif(op=="*"):
#     res=operator.mul(no1,no2)
#     print("Result:", res)
# elif(op=="/"):
#     res = div(no1, no2)
#     print("Result:", res)
# elif(op=="pow"):
#     res=operator.pow(no1,no2)       #res=no1**no2
#     print("Result:", res)
# elif(op=="log"):
#     res=math.log(no1,no2)   #Log of no1 with base no2
#     print("Result:", res)
# else:
#     print("Incorrect Operation")


"""Nested Conditions: Conditions inside conditions
Nested if: if inside if.....
"""
# a,b=7,7
# if(a==5):
#     if(b==6):
#         print("ABC")
#     else:
#         print("DEF")
# elif(a==6):
#     print("CETPA")
# elif(a==7):
#     if(b==8):
#         print("GHI")
#     elif(b==9):
#         print("JKL")
#     else:
#         print("LMN")


"""Logical Operators: 
and
or
not
"""
# a,b=5,8
# if(a==5 and b==7):
#     print("CETPA")
# else:
#     print("Hello")

# #New Program
# a,b=5,7
# print(a==b)

# """Find the Bigger of 2 numbers"""
# #BLL
# def compare(a,b):       #a,b=5,7
#     if(a>b):
#         return a
#     else:
#         return b
#
# #PL
# no1=int(input("Enter First No:"))
# no2=int(input("Enter Second No:"))
# res=compare(no1,no2)
# print("The Bigger number is:",res)

"""Find the Biggest of 3 numbers, without using logical operators"""
#BLL
# def compare(a,b,c):       #a,b=9,7,5
#     if(a>b):
#         if(a>c):
#             return a
#         else:
#             return c
#     else:
#         if(b>c):
#             return b
#         else:
#             return c
#
# #PL
# no1=int(input("Enter First No:"))
# no2=int(input("Enter Second No:"))
# no3=int(input("Enter Third No:"))
# res=compare(no1,no2,no3)
# print("The Biggest number is:",res)

"""Check whether a character input by user is capital or small, without using
string methods

Keyboard characters are saved in ASCII formats in the background
A: 65           a=97
B: 66           b=98
C: 67           c=99
.
.
Z: 90           z=122

ord(character)
chr(ASCII)
# """
# #New Program
# ch="A"
# print(ord(ch))

# #New Program
# ch=input("Enter Any Character:")        #z
# asc=ord(ch)
# if(asc>=65 and asc<=90):
#     print("The Entered character is a Capital Letter")
# elif(asc>=97 and asc<=122):
#     print("The Entered character is a Small Letter")
# else:
#     print("The Entered Character is not an English Alphabet")


# #New Program
# asc=ord("Z")
# print(asc)
# asc=asc+32
# ch=chr(asc)
# print(ch)

