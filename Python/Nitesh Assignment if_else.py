# 1. Take any Month Number as input from user and display Month name in the word.
# num1 = int(input("Enter month number :"))
# if(num1==1):
#     print("january")
# elif(num1==2):
#     print("february")
# elif(num1==3):
#     print("march")
# elif(num1==4):
#     print("april")
# elif(num1==5):
#     print("may")
# elif(num1==6):
#     print("june")
# elif(num1==7):
#     print("july")
# elif(num1==8):
#     print("august")
# elif(num1==9):
#     print("september")
# elif(num1==10):
#     print("october")
# elif(num1==11):
#     print("november")
# elif(num1==12):
#     print("december")
# else:
#     print("incorrect input")

# 2. Check if a Number is Positive, Negative or 0
# num1 = int(input("Enter the number :"))
# if (num1>0):
#     print("positive")
# elif(num1<0):
#     print("negative")
# else:
#     print("zero")

# 3. Take a single character as input from user. Check whether the character is an English Alphabet or a Number?
# ch = input("enter any character:")
# asc = ord(ch)
# if(asc>=65 and asc<=90 ):
#     print("entered character is an  capital letter english alphabet")f
# elif(asc>=97 and asc<=122):
#     print("entered character is an  small letter english alphabet")
# else:
#     print("number")

# 4. Take a single character as input from user. If the letter is upper case then convert it to lower case and print, else directly print the original character.
# Don’t use upper() method of string.

# ch = input("enter any character:")
# asc = ord(ch)
# if(asc>=65 and asc<=90):
#     asc= asc+32
#     low= chr(asc)
#     print(low)
# else:
#     print(ch)

# # 5. Make a Calculator with 10 operations
#
# #BLL
# import math
# import operator
# def add(a,b):
#     return a+b
# def sub(a,b):
#     return a-b
# def multiply(a,b):
#     return a*b
# def div(a,b):
#     return a/b
# def pow(a,b):
#     return a**b
# def log(a,b):
#     return math.log(a,b)
# def sin(a):
#     return math.sin(a)
# def cos(a):
#     return math.cos(a)
# def tan(a):
#     return math.tan(a)
# def remain(a,b):
#     return a%b
#
# #PLL
# num1 = int(input("Enter first no. "))
# num2 = int(input("Enter second no. "))
# opt = input("Enter operation '+','-','*','/','%','pow','log','sin','cos','tan' : ")
# if(opt=="+"):
#     res = add(num1,num2)
#     print("Result :",res)
# elif(opt=="-"):
#      res = sub(num1,num2)
#      print("Result :",res)
# elif(opt=="*"):
#      res = multiply(num1,num2)
#      print("Result :",res)
# elif(opt=="/"):
#      res = div(num1,num2)
#      print("Result :",res)
# elif(opt=="pow"):
#      res = pow(num1,num2)
#      print("Result :",res)
# elif(opt=="log"):
#      res = log(num1,num2)
#      print("Result :",res)
# elif(opt=="sin"):
#      res = sin(num1)
#      print("Result :",res)
# elif(opt=="cos"):
#      res = cos(num1)
#      print("Result :",res)
# elif(opt=="tan"):
#      res = tan(num1)
#      print("Result :",res)
# elif(opt=="%"):
#      res = remain(num1,num2)
#      print("Result :",res)
# else:
#      print("Wrong Input")

# 6. Find the Biggest of 4 numbers

#BLL
# def compare(a,b,c,d)
#     if(a>b):
#         if(a>c):
#             if(a>d):
#                 return a
#
#
#
#
#
#
# #PLL
# no1=int(input("Enter First No:"))
# no2=int(input("Enter Second No:"))
# no3=int(input("Enter Third No:"))
# no4=int(input("Enter fourth no.:"))
# res=compare(no1,no2,no3,no4)
# print("The Biggest number is:",res)


