""
"""
MultiElement: str, list and tuple

str  is a collection of homogeneous data type ie collection of characters only
list and tuple are collection of heterogeneous data type

list is mutable
tuple and str are immutable
"""
# #New Program
# s="CETPA"
# print(id(s))
# s1=s.lower()
# print(s1, s)
# print(id(s1), id(s))

# #New Program
# L1=[10,20,30]
# print(id(L1))
# L2=L1.extend([40,50])
# print(id(L1))
# print(L2)
# print(L1)

# #New Program
# def func1():
#     return 5
#
# r=func1()
# print(r)


# #New Program
# def func1():
#     pass
#
# r=func1()
# print(r)

# #New Program
# s="CETPA"
# print(s.lower())
# L=[10,20,30]
# print(L.extend([40,50]))        #L.extend:  None
# print(L)

# #New Program
# def func1(L):
#     L.append(40)
#
# L1=[10,20,30]
# L2=func1(L1)    #L=L1, formal parameter=actual parameter
# print(L1)
# print(L2)

# #New Program
# L=[10,20,30]
# print(id(L))
# L[1]=40
# print(id(L))

# #New Program
# L=[10,20,30,10,30,30,30,40]
# n=L.count(30)
# print(n)
# print(L.count(50))

# #New Program
# L=[10,20,30]
# L.insert(1,50)  #To add element at some particualr index
# print(L)

# #New Program
# L=[10,20,30,10,30,30,30,40]
# i=L.index(30)
# print(i)

# #New Program
# L=[10,20,30]
# L.clear()
# print(L)

# #New Program
# L=[10,20,30]
# L.pop()     #Last element will be deleted
# print(L)

# #New Program
# L=[10,20,30]
# e=L.pop()     #Last element will be deleted and it will return the deleted element
# print(L,e)

# #New Program
# L=[10,20,30]
# e=L.remove(20)  #remove method will delete the first element passed in the list
# print(L,e)

# #New Program
# L=[10,20,30,20]
# e=L.remove(20)
# print(L,e)

# #New Program
# L=[10,20,30,20]
# u=20
# e=L.remove(u)
# print(L,e)

# #New Program
# L=[10,20,30,20]
# L.reverse()
# print(L)

# #New Program
# L=[10,20,30,20]
# L.sort()
# print(L)

# #New Program
# L=[10,20,30,20]
# L.sort(reverse=True)
# print(L)

# #New Program
# s=input("Enter Mobile No:")
# print(s.isdecimal())

# s="CETPA"
# s.startswith()

# #New Program
# s=input("Enter Mobile No:")
# if(s.isdecimal() and len(s)==10):
#     print("Entered No is in Correct Format")
# else:
#     print("Incorrect Mobile No")


"""Infinte Loop
while(Any True Value):
    set of statement
    
False Values:
0
empty value like: empty string, empty list
False
None

Generally we create infinite loop:
while(1):
 set of statements
"""
# #New Program
# while("ABCD"):
#     print("CETPA")


# #New Program
# while(1):
#     s=input("Enter Mobile No:")
#     if(s.isdecimal() and len(s)==10):
#         print("Entered No is in Correct Format")
#         break
#     else:
#         print("Incorrect Mobile No, Enter the Correct no")

# #New Program
# L=[10,20,30]
# L.append(50)
# print(L)

# #New Program
# L=[10,20,30]
# L.extend(50)    #Error: Extend method only demands for iterators
# print(L)

# #New Program
# L=[10,20,30]
# s="CETPA"
# L.append(s)
# print(L)
# L=[10,20,30]
# L.extend(s)
# print(L)

# #New Program
# L=[10,20,30]
# L[1]=40
# print(L)

# #New Program
# L1=[10,20,30,40]        #Unique
# L2=["Ram","Vikas","Anil","Amit"]
# L3=[39,41,45,55]
# id=int(input("Enter Student ID:"))  #id=20
# i=L1.index(id)      #i=1
# print("Student Name:",L2[i],"Student Age:",L3[i])

# #New Program
# L2=["Ram","Vikas","Anil","Amit"]
# print(L2[1])

# #New Program
# L2=["Ram","Vikas","Anil","Amit"]
# i=1
# print(L2[i])

# #New Program
# L=[10,20,30]
# L.pop()  #By Default delete last element
# print(L)

# #New Program
# L=[10,20,30]
# L.pop(1)  #
# print(L)



# #New Program
# L1=[10,20,30,40]        #Unique
# L2=["Ram","Vikas","Anil","Amit"]
# L3=[39,41,45,55]
# id=int(input("Enter Student ID:"))  #id=20
# i=L1.index(id)      #i=L1.index(20), i=1
# L1.pop(i)       #L1.remove(id)
# name=L2.pop(i)
# L3.pop(i)
# print("Following Student deleted successfully:",name)
# print(L3)

# #New Program
# L2=["Ram","Vikas","Anil","Amit"]
# print(L2[1])
# L2[1]="Banti"
# print(L2)

# #New Program
# L2=["Ram","Vikas","Anil","Amit"]
# i=1
# name=input("Enter updated name:")
# L2[i]=name
# print(L2)

# #New Program: Modify Student
# L1=[10,20,30,40]        #Unique
# L2=["Ram","Vikas","Anil","Amit"]
# L3=[39,41,45,55]
# id=int(input("Enter Student ID:"))  #id=20
# name=input("Enter Update Name:")    #name=Banti
# age=int(input("Enter Updated Age:"))    #age=42
# ind=L1.index(id)    #id=20, ind=1, n=L2[ind]
# L2[ind]=name
# L3[ind]=age
# print(L1,L2,L3)
# print("Student Data Updated Successfully")


# #New Program
# L1=[10,20,30,40]
# for e in L1:
#     print(e)

# #New Program
# L1=[10,20,30,40]
# for i in range(len(L1)):        #0,1,2,3
#     print(L1[i])

# #New Program
# L1=[10,20,30,40]        #Unique
# L2=["Ram","Vikas","Anil","Amit"]
# for i in range(len(L1)):    #i=0,1,2,3
#     print("Student Id:",L1[i],"Student Name:",L2[i])

"""
Next Class on Monday

"""
# idlist=[10,20,30]
# id=input("Enter Cust Id to Add:")
# if(id in idlist):
#     print("Id already Exists")
# else:
#     pass

# #New Program
# idlist=[10,20,30]
# id=input("Enter Cust Id to Add:")
# count=idlist.count(id)
# if(count==1):
#     print("Id already Exists")
# else:
#     pass

#New Program

