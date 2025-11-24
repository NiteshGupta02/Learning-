""
"""
14741

0   0  -1
1   1  -2
"""
# a=2345432
# a=str(a)    #a="14741"        #a=234432
# for i in range(len(a)//2):
#     if(a[i]!=a[-i-1]):
#         print("No is not Palindrome")
#         break
# else:
#     print("No is Palindrome")


#New Program
"""Take two numbers as input from the user and Print all the Prime Numbers 
between the numbers given by users using while loop.
5 and 13

"""
# #New Program
# r1=int(input("Enter Lower Value:"))     #r1=5
# r2=int(input("Enter Upper Value:"))     #r2=13
# flag=0
# for n in range(r1,r2+1):    #5 to 13, n=5, range(5,14)
#     for i in range(2,n):    #n=5, i=2,3,4
#         if(n%i==0):
#             flag=1
#             break
#     if(flag==0):
#         print(n," is Prime")
#     else:
#         flag=0

"""List: is a collection of heterogeneous data type
tuple: is a collection of heterogeneous data type
list is mutable and tuple is immutable

list, dict and set are mutable data types in python ie if change
elements of these data types ie either we edit, or increase or decrease
elements of mutable data types then new variables are not created.

Rest int,float,complex,bool,str,tuple,frozenset are immutable ie if we
try to modify elements of these variables then error will be generated.

So if we try to modify elements of immutable types then error still if we
want then we can create new variables.
"""
#New Program
# a=5
# print(a)
# b=a
# print(a,b)      #5,5
# a=7
# print(a,b)      #7,5

# #New Program
# a="CETPA"
# print(a)
# b=a
# print(a,b)      #CETPA, CETPA
# a="HELLO"
# print(a,b)      #HELLO CETPA

# #New Program
# a=[10,20,30]
# print(a)
# b=a
# print(a,b)      #[10,20,30] [10,20,30]
# print(id(a),id(b))
# a=[50,60,70]
# print(a,b)      #[50,60,70] [10 20 30]
# print(id(a),id(b))

# #New Program
# a=(10,20.5,"CETPA")
# print(a)
# print(type(a))


"No Negative Marking"
# #New Program
# a=[10,20,30]
# print(a)
# b=a     #b and a adress 1000
# print(a,b)      #[10,20,30] [10,20,30]
# print(id(a),id(b))
# a[0]=40     #List is mutable means we can modify elements of list
# print(a,b)      #[40,20,30] [10 20 30]
# print(id(a),id(b))

# #New Program
# a=(10,20,30)
# print(a)
# b=a
# print(a,b)      #(10,20,30) (10,20,30)
# a[0]=40         #Error
# print(a,b)      #

# #New Program
# a=(10,20,30)
# print(a)
# b=a
# print(id(a),id(b))
# print(a,b)      #(10,20,30) (10,20,30)
# a=(40,50,60)
# print(a,b)
# print(id(a),id(b))

"""Python supports dynamic memory allocation. Whenever we assign a new value
to a variable then new variables are created ie new values are stored at new
location and variable starts referring to new location. This rule is applicable
to all variables in Python either mutable or immutable
How variables are created in Python: By assigning a value. 
All variables in Python are of reference type: Whenever we assign one variable
to another then address of RHS variable is assigned to LHS variable 

"""

# a="CETPA"
# a[0]="M"    #Error , str is immutable
# print(a)

# #New Program
# a="CETPA"
# print(id(a))
# a="M"+a[1:]
# print(id(a))
# print(a)

# #New Program
# a=[10,20,30]
# print(id(a))
# a[0]=50
# print(id(a))  #Samme ID

# #New Program
# a=[10,20,30]
# print(id(a))
# a=[40,50,60]
# print(id(a))  #Samme ID

"""List Methods
Functions which are created outside class are called functions and can be
called by function_name(arguments)

Functions which are created inside class are preferable called methods. 
Methods can be called by object_name.method_name(arguments) 

"""
#New Program
# a="CETPA"   #Object is created of string type
# r=a.upper() #upper is a method defined inside string class
# print(r)

# # New Program
# a="Vikas Kumar Kalra"   #Object is created of string type
# r=a.split()
# print(r)

# #New Program
# L=['Vikas', 'Kumar', 'Kalra']
# print(L.swapcase())     #Error

# #New Program
# L1=[10,20,30]   #L1 address 1000
# print(id(L1))   #1000
# L2=L1           #L2 address 1000
# L1[0]=40        #L1 address 1000
# print(id(L1),id(L2))
# print(L1, L2)  #Same
# #New Program
# L1=[10,20,30]   #L1 address 1000
# print(id(L1))   #1000
# L2=L1.copy()        #Different address, L2=list(L1)
# print(id(L1),id(L2))
# L1[0]=40        #L1 address 1000
# print(L1, L2)  #Same

# #New Program
# L1=[10,20,30]
# L1.append(50)
# print(L1)
# L1.append([50,60,70])
# print(L1)
#
# #New Program
# L1=[10,20,30]
# L1.extend([50,60,70])
# print(L1)
