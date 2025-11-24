""
"""
Any question or doubt?
Question: In a string there are only alphabets and spaces.
if any isalpha or isspace
"""
# #New Program
# L1=[2,3,4,5,6,7,8]
# L2=[e%2==0 for e in L1]
# print(L2)
# res1=all(L2)
# print(res1)
# res2=any(L2)
# print(res2)

# #New Program
# L1=[2,4,6,8]
# L2=[e%2==0 for e in L1]
# print(L2)
# res1=all(L2) #If all the elements of iterator are True then result is True
# print(res1)
# res2=any(L2) #Atleast one element of iterator is True then result is True
# print(res2)


# #New Program
# s="Vikas Kumar Kalra"
# res=all([(e.isalpha() or e.isspace()) for e in s])
# print(res)

"""
New concepts in comprehension were added later
and Comprehension now supports
list comprehension
set comprehension
dict comprehension
generator comprehension
"""
# #New Program
# L1=[2,3,4,5,6,7,8,2,3,5,6]
# s={e**2 for e in L1 if e%2==0}
# print(s)

# #New Program: Dictionary Comprehension
# L1=[2,3,4,5,6,7,8,2,3,5,6]
# s={e:e**2 for e in L1 if e%2==0}
# print(s)


"""
There is no negative marking in our class.

Embedded System: Small size processor, ROM, RAM, ports are fabricated
on single IC. When we download small applications in ROM, then
applications executes line by line.

But for the bigger systems, firstly we install an OS inside the system. 
And on top of the OS, we install the applications. 
Why we install OS? 
Why OS was created: OS was designed to provide the event scheduling in the
program. It run multiple application at same time, though multiple applications
are not executed simultaneously rather OS provides event scheduling which
gives the user, a feel that all applications are running simultaneously.
OS provides a feel of multi-tasking systems ie multiple tasks are executing
parallely. 

Thread is a smallest unit of code, which can be fetched to CPU directly.
Threads are functions in programming.

Multi-Tasking Systems are of two types: 
MultiThreading: In multi-threading systems, we run the threads parallely.
So parallel means fast speed events scheduling. To run multiple functions
parallely, means OS gives time to threads ie multiple functions, one by
one but at a very high speed.

MultiProcessing: In multi-processing systemms, we run multiple processes
at the same time.

Thread: small code, a function
Threads can share the resources with other threads

Process: Bigger code or application. Processes don't share the resources
with other processes

One Process can have multiple threads inside it.
"""
# #New Program
# L1=[3,4,5]
# # L2=L1+6     #Error
# L2=[6,7,8]
# L3=L1+L2
# print(L3)

#New Program
# import numpy as np
# arr=np.array([2,3,4,5])
# print(arr)
# print(type(arr))
# a=arr+3         #Broadcasting in ndarray: Element by Element Addition
# print(a)


# #New Program
# def func1(a,b):
#     r=a+b
#     return r
# def func2(a,b):
#     r=a-b
#     return r
# m,n=5,7
# s1=func1(m,n)
# s2=func2(m,n)
# print(s1,s2)


# #New Program
# import threading
# def func1():
#     print("CETPA")
# def func2():
#     print("Infotech")
# th1=threading.Thread(target=func1)
# th2=threading.Thread(target=func2)
# th1.start()
# th2.start()
# print("Pvt. Ltd.")

"""
By Default in any program, once we run the program, 
one thread will be automatically created ie Main Thread.
Now manually, we need to start other thread using 
thread_name.start().
Now OS will do event scheduling and will start giving time/control to
all threads at a very fast pace.   
"""

# #New Program
# import threading
# def func1():
#     for i in range(100):
#         print("Thread1: CETPA",i)
# def func2():
#     for i in range(100):
#         print("Thread 2: Infotech",i)
# th1=threading.Thread(target=func1)
# th2=threading.Thread(target=func2)  #Till now only main thread is running
# th1.start()     #2 threads are started ie Main Thread and thread 1
# th2.start()     #3 threads are started if Thread 1 is still alive
# for i in range(100):
#     print("MainThread: Pvt. Ltd.",i)

# #New Program
# import threading
# def func1():
#     global a
#     for i in range(10000000):
#         a+=1
# def func2():
#     global b
#     for i in range(10000000):
#         b+=1
# a,b=0,0
# th1=threading.Thread(target=func1)
# th2=threading.Thread(target=func2)
# th1.start()
# th2.start()
# print(a,b)      #Any value between 0 and 100
# print(th1.is_alive())
# print(th2.is_alive())

# #New Program
# import threading
# def func1():
#     global a
#     for i in range(10000000):
#         a+=1
# def func2():
#     global b
#     for i in range(10000000):
#         b+=1
# a,b=0,0
# th1=threading.Thread(target=func1)
# th2=threading.Thread(target=func2)
# th1.start()
# th2.start()
# while(th1.is_alive() or th2.is_alive()):
#     pass
# print(th1.is_alive(), th2.is_alive())
# print(a,b)      #Any value between 0 and 100


"""
join method, binds the particular thread with main thread. Now till the time
that particular thread is alive, main_thread won't run, OS won't give time to this
thread. ie your python program, requests OS to give time to all its threads and now
your python program will put the main thread in pause state, once that particular
thread is killed, now main thread will be alive again and OS will start giving time to
main thread also.
After using join method, only particular thread will be bound with main thread though
all other threads will keep on running and only main thread will be paused till the
time the particular thread which was bound, is alive.  

"""
# #New Program
# import threading
# def func1():
#     global a
#     for i in range(10000000):
#         a+=1
# def func2():
#     global b
#     for i in range(10000000):
#         b+=1
# a,b=0,0
# th1=threading.Thread(target=func1)
# th2=threading.Thread(target=func2)
# th1.start()
# th2.start()
# th1.join()     # now 2 threads will be running ie th1 and th2
# th2.join()      #now only 1 thread ie th2
# print(th1.is_alive(), th2.is_alive())
# print(a,b)