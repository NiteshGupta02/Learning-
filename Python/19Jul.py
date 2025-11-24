""
import M2

"""
Module
We have different option to access user defined modules or predefined
modules
"""

# #New Program: Syntax1
# import Module1
# r1=Module1.add(5,7)
# print(r1)
# r2=Module1.m*Module1.n
# print(r2)

# #New Program: Syntax2
# import Module1 as M1
# r=M1.add(5,7)
# print(r)

# #New Program: Syntax3
# from Module1 import add
# r1=add(5,7)
# print(r1)

# #New Program: Syntax4
# from Module1 import *
# r1=add(5,7)
# r2=sub(3,4)
# print(r1,r2)

# #New Program: Syntax5
# from Module1 import add as ad
# r1=ad(5,7)
# print(r1)

#New Program
# import Module1
# from Module1 import *
# from Module1 import add
# from Module1 import add as ad
# import Module1 as M1

# #New Program
# a=5
# a=7
# print(a)
# #New Program
# def func1(a,b):
#     return a+b
#
# c,d=5,7
# print(func1(c,d))
# print(func1)
# print(type(func1))


# #New Program
# def func1(a,b):     #<function func1 at 0x00000239568804A0>
#     print(a+b)
# print(func1)
# def func1(a,b):     #<function func1 at 0x000001EBE7CBC680>
#     print(a*b)
# print(func1)


# #New Program
# from operator import *
# from M2 import *
# r=sub(5,7)
# print(r)

# #New Program
# import operator as op
# import M2 as M
# r1=M2.sub(5,7)
# r2=op.sub(5,7)
# print(r1,r2)

# #New Program
# import M3       #ModuleNotFoundError: No module named 'M3'

# #New Program
# print(r"CE\n\nTPA")     #r: Raw String

# #New Program
# import sys
# print(sys.path)
# print(type(sys.path))
# print(len(sys.path))
# sys.path.append(r"D:\Vikas")
# print(sys.path)
# import M3
# print(M3.add(5,7))

# #New Program
# import sys
# print(sys.version)
# print(sys.version_info)

# #New Program
# def func1():
#     global a
#     a=5
#     print(a)
#
# func1()
# print(a)

# #New Program
# from M4 import add

#New Program
import M4
# print(__name__)

"""
__name__ 
Whenever we run a program in Python then that program is represented by name 
as '__main__' and other modules are represented by their actual names. 
While execution of the program __name__ variable represents the file name which
is executed at particular point of time.

"""


"""
module/package/library/framework 
"""
# #New Program
# import Lib1.Mod1
# r=Lib1.Mod1.add(5,7)
# print(r)

# #New Program
# import Lib1.Mod1 as M1
# r=M1.add(5,7)
# print(r)

# #New Program
# from Lib1 import Mod1,Mod2
# r1=Mod1.add(5,7)
# r2=Mod2.mul(2,3)
# print(r1,r2)

# #New Program
# from Lib1.Mod1 import *
# r=add(5,7)
# print(r)



