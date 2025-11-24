""
"""
How to create your own iterators and generators:

Iterator: is a data type on which we can run a loop:

How loop runs:
for element in iterator:
    pass
    
Steps:

1. iterator.__iter__ method call, it returns the object of iterator.
2. on iterator object, every time __next__ method is called
3. Once all the elements are received, a StopIteration error is raised
and this error is caught by loop and loop breaks and control comes
out of the loop   
"""
# L1=[2,3,4]
# # for e in L1:
# #     print(e)
# iter_obj=L1.__iter__()
# e=iter_obj.__next__()
# print(e)
# e=iter_obj.__next__()
# print(e)
# e=iter_obj.__next__()
# print(e)
# e=iter_obj.__next__()
# print(e)


# #New Program
# class myIterator:
#     def __iter__(self):
#         return self
#     def __next__(self):
#         global a
#         if(a==6):
#             raise StopIteration
#         else:
#             temp=a
#             a+=1
#             return temp
# a=3
# for e in myIterator():
#     print(e)


# #New Program
# L1=[2,3,4]      #L1 is iterable, object of list class
# print(type(L1))
# obj=L1.__iter__()   #obj is iterator ie object of list_iterator
# print(type(obj))
# print(obj.__next__())
# print(obj.__next__())
# print(obj.__next__())

"""We can pass only integers in range class"""
# #New Program
# for i in range(2,5,0.5):    #Error
#     print(i)

# #New Program
# for i in range(2,5,2):
#     print(i)

"""
We want to create our own range iterator which should work on all +ve
float values
"""
# for i in range(5,2,2):
#     print(i)

# #New Program
# class myFloatRange:
#     def __init__(self,start,stop,step):     #Parameterized Constructor
#         self.start=start
#         self.stop=stop
#         self.step=step
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if(self.start>=self.stop):
#             raise StopIteration
#         temp=self.start     #temp=2, 2.5...4.5
#         self.start+=self.step   #self.start=2.5, 3, ....5
#         return temp
# for i in myFloatRange(2,5,0.5):
#     print(i)


# #New Program
# class myFloatRange:
#     def __init__(self,start,stop=None,step=1):     #Parameterized Constructor
#         if(stop==None):
#             self.start=0
#             self.stop=start
#         else:
#             self.start=start
#             self.stop=stop
#         self.step=step
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if(self.start>=self.stop):
#             raise StopIteration
#         temp=self.start     #temp=2, 2.5...4.5
#         self.start+=self.step   #self.start=2.5, 3, ....5
#         return temp
# for i in myFloatRange(2,4,0.5):
#     print("First Loop:",i)
# for i in myFloatRange(2,4):
#     print("Second Loop:",i)
# for i in myFloatRange(3):
#     print("Third Loop:",i)

# #New Program
# L1=[2,3,4]
# m1=L1.__sizeof__()
# print(m1)
# m2=L1[0].__sizeof__()
# print(m2)
# m3=L1[1].__sizeof__()
# print(m3)
# m4=L1[2].__sizeof__()
# print(m4)
# total_mem=m1+m2+m3+m4
# print(total_mem)

"""
How to create your own generators:

generators: are the functions having at least 1 yield statement 
inside the function.

1. generators are like iterators and we can run loop on generators
2. generators create __iter__ and __next__ method as well StopIteration
Error in the background, user/developer need not to create it.
3. Now every time we call the generator, values from the generator
will be retrieved through yield statement and not through return
4. If we put yield statement inside a function then function holds
the values of variables till the time generator is executing (ie till
the time loop is running), ie the state of the variables will be maintained
and garbage collector won't delete/kill/destroy them  

 
"""
# #New Program
# def func1():
#     return 1
# print(type(func1))

# #New Program
# def func1():
#     return 1
# print(type(func1()))


# #New Program
# def func1():
#     yield 1
# print(type(func1()))

# #New Program
# def myGenerator():
#     yield 1
#     yield 2
#     yield 3
# for i in myGenerator():
#     print(i)


# #New Program
# r=range(0,5)
# print(r)
# L=list(r)
# print(L)


# #New Program
# def myGenerator(r):
#     for i in range(r):
#         yield i
# for i in myGenerator(4):
#     print(i)
# #New Program
# L=list(myGenerator(4))
# print(L)

# #New Program
# class C1:
#     pass
# obj=C1()
# print(obj)
# i=int()
# print(i)
# r=range(5)
# print(r)

"""Each class is having __str__ method or its parent can have __str__ method
Whenever we print any type of data in python then firstly it is converted
to string type by calling obj.__str__() method
"""
# a,b=5,2.5
# c=b.__str__()
# print(type(c), c)
# print(a,b)      #print(a.__str__(),b.__str__)

# class C1:
#     def __str__(self):
#         return "CETPA"
# ob=C1()
# print(ob)       #print(ob.__str__())

# #New Program
# class C1:
#     def __str__(self):
#         return 5
# ob=C1()
# print(ob)       #print(ob.__str__())    #Error

#New Program
"""Generator"""

# #New Program
# def myFloatRange(start,stop=None,step=1): # start=4,stop=None
#     if(stop==None):
#         start=0         #start=0
#         stop=start      #stop=4
#     while(start<stop):  #start yes
#         temp=start      #temp=0
#         start+=step     #start=1
#         yield temp
# for i in myFloatRange(4):
#     print("First Loop:",i)
