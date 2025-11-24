
# def add(a,b):
#     r=a+b
#     return r
#
# m,n=5,7
# s=add(m,n)
# print("Result:",s)

# #New Program
# def func1(L1):
#     L1.append(5)
#     L1.append(6)
#
# L2=[2,3,4]
# func1(L2)
# print(L2)

"""
Exception Handling: Handling of the Errors

Exception: Errors
4 Keywords associated with Exception Handling in Python
try: This keyword keep on eye on the complete code inside try block and if
there is an error in any particular line of the code, try will catch this error
and will send the control of the program to except block. try block atleast
need except block along with try block. 
except
finally
raise

"""
# #New Program
# L1=[2,3,4]
# print(L1[7])  #IndexError: list index out of range

# #New Program
# L1="CETPA"
# print(L1[7])        #IndexError: string index out of range

# #New Program
# idlist=[10,20,30,40,50]
# index=idlist.index(70)      #ValueError: 70 is not in list
# print(index)

# #New Program
# import mathlib      #ModuleNotFoundError: No module named 'mathlib'


# #New Program
# while(1):
#     try:
#         idlist=[10,20,30]
#         id=int(input("Enter Customer ID:"))
#         index=idlist.index(id)
#         print(index)
#         break
#     except:
#         print("Id Not Found")

# #New Program
# n=int(input("Enter Any Number:"))   #ValueError: invalid literal for int() with base 10: '$'


# #New Program
# while(1):
#     try:
#         idlist=[10,20,30]
#         id=int(input("Enter Customer ID:"))
#         index=idlist.index(id)
#         print(index)
#         break
#     except ValueError as err:   #err object of ValueError Class
#         print(err)

"""Exception Class is the Parent to All Error Classes"""

# #New Program
# while(1):
#     try:
#         idlist=[10,20,30]
#         id=int(input("Enter Customer ID:"))
#         index=idlist.index(id)
#         print(index)
#         break
#     except Exception as err:   #err object of ValueError Class
#         print(err, type(err))


# #New Program
# while(1):
#     try:
#         idlist=[10,20,30]
#         id=int(input("Enter Customer ID:"))
#         index=idlist.index(id)
#         print(index)
#         break
#     except ValueError as err:   #err object of ValueError Class
#         print("Error!",err)
#     except Exception as err:
#         print("Error!",err)


# #New Program: Addition of two numbers
# while(1):
#     try:
#         n1=int(input("Enter First No:"))
#         n2=int(input("Enter Second No:"))
#         res=n1+n2
#         print("Result:",res)
#         break
#     except ValueError:
#         print("Enter Inputs in Whole Numbers Only")
#     except Exception as err:
#         print("Error!",err)

# #New Program: Scientific Calci
# import math
# import operator
# def add(a,b):
#     return a+b
# def sub(a,b):
#     return a-b
# def div(a,b):
#     return a/b
# #PL
# while(1):
#     try:
#         no1=int(input("Enter First No:"))
#         no2=int(input("Enter Second No:"))
#         ch=input("Enter Choice +, -, *, /, pow, log,exit:")
#         if(ch=="+"):
#             res=add(no1,no2)
#             print("Result:",res)
#         elif(ch=="-"):
#             res=sub(no1,no2)
#             print("Result:",res)
#         elif(ch=="*"):
#             res=operator.mul(no1,no2)       #res=no1*no2
#             print("Result:",res)
#         elif(ch=="/"):
#             res=div(no1,no2)
#             print("Result:",res)
#         elif(ch=="pow"):
#             res=operator.pow(no1,no2)
#             print("Result:",res)
#         elif(ch=="log"):
#             res=math.log(no1,no2)
#             print("Result:",res)
#         elif(ch=="exit"):
#             break
#         else:
#             print("Incorrect Choice")
#     except ValueError:
#         print("Error! Enter Inputs in Whole Numbers Only")
#     except ZeroDivisionError:
#         print("Error! Enter Non Zero Second Input")
#     except Exception as err:
#         print("Error!",err)

"""finally keyword:
finally is the block of code which executes everytime, whether exception is
there or exception is not there

"""
# #New Program: Scientific Calci
# import math
# import operator
# def add(a,b):
#     return a+b
# def sub(a,b):
#     return a-b
# def div(a,b):
#     return a/b
# #PL
# while(1):
#     try:
#         no1=int(input("Enter First No:"))
#         no2=int(input("Enter Second No:"))
#         ch=input("Enter Choice +, -, *, /, pow, log:")
#         if(ch=="+"):
#             res=add(no1,no2)
#             print("Result:",res)
#         elif(ch=="-"):
#             res=sub(no1,no2)
#             print("Result:",res)
#         elif(ch=="*"):
#             res=operator.mul(no1,no2)       #res=no1*no2
#             print("Result:",res)
#         elif(ch=="/"):
#             res=div(no1,no2)
#             print("Result:",res)
#         elif(ch=="pow"):
#             res=operator.pow(no1,no2)
#             print("Result:",res)
#         elif(ch=="log"):
#             res=math.log(no1,no2)
#             print("Result:",res)
#         else:
#             print("Incorrect Choice")
#     except ValueError:
#         print("Error! Enter Inputs in Whole Numbers Only")
#     except ZeroDivisionError:
#         print("Error! Enter Non Zero Second Input")
#     except Exception as err:
#         print("Error!",err)
#     finally:
#         cont=input("Press Y to Continue:")
#         if(cont!="Y" and cont!="y"):
#             break

"""No Practise No Learning"""
#New Program
"""
DS/DA/BA: Tool ya DA using Python
Full Stack: Web Designing or Django

raise Keyword: To raise the exceptions forcefully



"""
# #New Program: Scientific Calci
# import math
# import operator
# def add(a,b):
#     return a+b
# def sub(a,b):
#     return a-b
# def div(a,b):
#     return a/b
# #PL
# while(1):
#     try:
#         no1=int(input("Enter First No:"))
#         no2=int(input("Enter Second No:"))
#         ch=input("Enter Choice +, -, *, /, pow, log:")
#         if(ch=="+"):
#             res=add(no1,no2)
#             print("Result:",res)
#         elif(ch=="-"):
#             res=sub(no1,no2)
#             print("Result:",res)
#         elif(ch=="*"):
#             res=operator.mul(no1,no2)       #res=no1*no2
#             print("Result:",res)
#         elif(ch=="/"):
#             res=div(no1,no2)
#             print("Result:",res)
#         elif(ch=="pow"):
#             res=operator.pow(no1,no2)
#             print("Result:",res)
#         elif(ch=="log"):
#             res=math.log(no1,no2)
#             print("Result:",res)
#         else:
#             #print(Incorrect Choice")
#             raise NotImplementedError("Incorrect Choice")
#     except ValueError:
#         print("Error! Enter Inputs in Whole Numbers Only")
#     except ZeroDivisionError:
#         print("Error! Enter Non Zero Second Input")
#     except NotImplementedError as err:
#         print("Error!",err)
#     except Exception as err:
#         print("Error!",err)
#     finally:
#         cont=input("Press Y to Continue:")
#         if(cont!="Y" and cont!="y"):
#             break





