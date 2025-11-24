""
"""
Inheritance: Accessing the properties/attributes (variables and methods) 
from one class to another class

"""
# class C1:
#     def __init__(self):
#         self.a=1
#         self.b=2
#     def showData(self):
#         print(self.a,self.b,"I am in Class C1")
# class C2(C1):       #C2 child and C1 parent
#     def __init__(self):
#         self.c=3
#         self.d=4
#         super().__init__()
#     def showData(self):
#         print(self.a,self.b,self.c,self.d,"I am in Class C2")
# ob=C2() #ob=1000,
# ob.showData()

"""
Type of Inheritance:
1. Single Level Inheritance: One Parent, One Child
2. Multi Level Inheritance: One Parent having one child, child is having
another child, next child is having next child...
3. Hieraichal Inheritance: One Parent multi children
4. Multiple Inheritance: One Child, Multi Parents
5. Hybrid Inheritance: Mixed of above
"""

# "2. Multi Level Inheritance:"
# #New Program
# class C1:
#     def __init__(self):
#         self.a=1
#         self.b=2
#     def showData(self):
#         print("I am in Class C1")
# class C2(C1):
#     def __init__(self):
#         self.c=3
#         self.d=4
#         super().__init__()
#     def showData(self):
#         print("I am in Class C2")
# class C3(C2):
#     def __init__(self):
#         self.e=5
#         self.f=6
#         super().__init__()
#     def showData(self):
#         print("I am in Class C3")
# ob=C3()
# print(ob.a,ob.b,ob.c,ob.d,ob.e,ob.f)
# ob.showData()

"2. Hierarchical Inheritance:"
# #New Program
# class C1:
#     def __init__(self):
#         self.a=1
#         self.b=2
#     def showData(self):
#         print("I am in Class C1")
# class C2(C1):
#     def __init__(self):
#         self.c=3
#         self.d=4
#         super().__init__()
#     def showData(self):
#         print("I am in Class C2")
# class C3(C1):
#     def __init__(self):
#         self.e=5
#         self.f=6
#         super().__init__()
#     def showData(self):
#         print("I am in Class C3")
# class C4(C1):
#     def __init__(self):
#         self.g=7
#         self.h=8
#         super().__init__()
#     def showData(self):
#         print("I am in Class C4")
# ob=C4()
# # print(ob.a,ob.b,ob.c,ob.d,ob.e,ob.f,ob.g,ob.h)   #Error
# print(ob.a,ob.b,ob.g,ob.h)
# ob.showData()

"""Diamond Problem ie in case of multiple inheritance if one child is having
multiple parents, and there are methods with same name in all parents, and child
is not having the method with that name, now if we call the parent method then
it creates an ambiguity that which parent method will be given the preference,
and due to this ambiguity Java doesn't support multiple inheritance and to 
achieve multiple inheritance is java, another concept of interface is designed.
And this ambiguity problem is called diamond problem

But python supports multiple inheritance and it gives a priority to parents,
and in case if user (developer) feels any ambiguity then a special variable ie
__mro__ variable is created to given the right solution to suggest the parent
whose method will be given the priority

To achieve multiple inheritance:
Mention all parents in bracket of child class.
Then call all the parents constructors from child constructor.
Syntax can be
super().__init__() #Here super will refer to first parent mentioned in bracket of child class
Class_Name.__init__(self)

__mro__: Method Resolution Operator: If you feel any ambiguity in accessing
a method then mro will let us know the right sequence of methods that would
be called

In multiple languages, all predefined or user defined classes have one common
parent ie object class, this parent is automatically created.
object class is the parent to all user defined and predefined classes.
"""
# #New Program
# L1=[2,3,4]
# L1.append(5)    #Object_name.method_name(arguments)
# print(L1)

# #New Program
# L1=[2,3,4]
# list.append(L1,5)    #Object_name.method_name(arguments)
# print(L1)


# #New Program
# class C1:
#     def __init__(self):
#         self.a=1
#         self.b=2
#     # def showData(self):
#     #     print("I am in Class C1")
# class C2:
#     def __init__(self):
#         self.c=3
#         self.d=4
#     # def showData(self):
#     #     print("I am in Class C2")
# class C3:
#     def __init__(self):
#         self.e=5
#         self.f=6
#     def showData(self):
#         print("I am in Class C3")
# class C4(C1,C2,C3):
#     def __init__(self):
#         self.g=7
#         self.h=8
#         super().__init__()
#         C2.__init__(self)
#         C3.__init__(self)
#     # def showData(self):
#     #     print("I am in Class C4")
# ob=C4()
# ob.showData()
# print(ob.a,ob.b,ob.c,ob.d,ob.e,ob.f,ob.g,ob.h)
# # print(ob.a,ob.b,ob.g,ob.h,ob.c)
# # ob.showData()
# print(C4.__mro__)

# "Hybrid Inheritance"
# #New Program
# class C1:
#     def __init__(self):
#         self.a=1
#         self.b=2
#     def showData(self):
#         print("I am in Class C1")
# class C2(C1):
#     def __init__(self):
#         self.c=3
#         self.d=4
#         super().__init__()
#     # def showData(self):
#     #     print("I am in Class C2")
# class C3(C1):
#     def __init__(self):
#         self.e=5
#         self.f=6
#         super().__init__()
#     # def showData(self):
#     #     print("I am in Class C3")
# class C4(C2,C3):
#     def __init__(self):
#         self.g=7
#         self.h=8
#         super().__init__()
#         C3.__init__(self)
#     # def showData(self):
#     #     print("I am in Class C4")
# ob=C4()
# ob.showData()
# print(ob.a,ob.b,ob.c,ob.d,ob.e,ob.f,ob.g,ob.h)
# # print(ob.a,ob.b,ob.g,ob.h,ob.c)
# # ob.showData()
# # print(C4.__mro__)


"Hybrid Inheritance"
# #New Program
# class C1:
#     def __init__(self):
#         self.a=1
#         self.b=2
#     def showData(self):
#         print("I am in Class C1")
# class C2(C1):
#     def __init__(self):
#         self.c=3
#         self.d=4
#         super().__init__()
#     # def showData(self):
#     #     print("I am in Class C2")
# class C3:
#     def __init__(self):
#         self.e=5
#         self.f=6
#     def showData(self):
#         print("I am in Class C3")
# class C4(C2,C3):
#     def __init__(self):
#         self.g=7
#         self.h=8
#         super().__init__()
#         C3.__init__(self)
#     # def showData(self):
#     #     print("I am in Class C4")
# ob=C4()
# ob.showData()
# print(ob.a,ob.b,ob.c,ob.d,ob.e,ob.f,ob.g,ob.h)
# # print(ob.a,ob.b,ob.g,ob.h,ob.c)
# # ob.showData()
# print(C4.__mro__)

"""
Debugging your code:
To execute your code line by line
Steps:
1. Create the start point to debug the code ie click on left pane, on
the line number, from where the debugging to start, it is called
a breakpoint or a bubble
2. Right click, and ISO run the code, rather debug the code
3. Now press F7 or F8 to run the code line by line
F7: To jump inside the funciton call (if any)
"""
# #New Program
# def add(a,b):
#     r=a+b
#     return r
# m,n=2,3
# s=add(m,n)
# print("Result:",s)

"""
Access Specifier or Access Modifiers: To specify, at what places, a 
particular attribute (variable or method) can be accessed in class.
In Python we have three types of access specifiers
Public
Protected
Private
In Python we can access all private/protected/public variables/methods
anywhere. Public/Protected attributes can be accessed directly. 
Private attribute can be accessed as:   object_name._classname__attributename

In Python, there is convention:
Public Attribute: Define directly
Protected Attribute: Put underscore before attribute name
Private Attribute: Put double underscore before attribute name


In Java or other OOPS based programming languages or in real OOPS, 
Public attribute can be accessed anywhere
Protected attribute can be accessed only in class itself or child class
Private attribute can only be accessed in class itself

"""
# class C1:
#     def __init__(self):
#         self.a=1        #Public
#         self._b=2       #Protected
#         self.__c=3      #Private
# ob=C1()
# print(ob.a)
# print(ob._b)
# # print(ob.__c)   #AttributeError: 'C1' object has no attribute '__c'
# print(ob._C1__c)

