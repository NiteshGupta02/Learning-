
"""
No Practise No Learning
"""
"""
Lambda Function:
1. Single Liner Functions: Can return single expression without
any function block statements
2. Anonymous Functions: These functions don't have any name
3. Return Object Address

Syntax
lambda arguments_passed:expression_returned
"""
# def add(a,b):
#     r=a+b
#     return r        #return a+b
# m,n=5,7
# s=add(m,n)
# print(s)

# #New Program
# def add(a,b):
#     r=a+b
#     return r        #return a+b
# m,n=5,7
# print(add(m,n))
# print(add)
# s=add
# print(s)
# print(s(5,7))


# #New Program
# a,b=5,7
# print(lambda a,b:a+b)   #lambda object address


# #New Program
# a,b=5,7
# s=lambda a,b:a+b
# print(type(s))
# print(s(5,7))

# #New Program
# a,b=5,7
# add=lambda a,b:a+b
# print(type(add))
# print(add(5,7))

# #New Program
# sq=lambda a:a**2
# print(sq(5))

"""
map function: in place of loop, if we want to perform any
particular operation on all the elements of iterator then we
can use map function

map(function_object,iterator)
map function returns the map object ie address of map object

If we want to convert the result to some predefined iterator
then we can type cast the map object
"""
"""
Create a new list having square of the elements of list
"""
# #New Program
# L1=[2,3,4,5,6,7,8]
# L2=[]
# for e in L1:
#     t=e*e
#     L2.append(t)
# print(L2)

# #New Program
# def sq(a):
#     return a**2
#
# L1=[2,3,4,5,6,7,8]
# m=map(sq,L1)    #m is the map object and this is also an iterator
# print(m)
# L2=list(m)
# print(L2)

# #New Program
# def sq(a):
#     return a**2
# L1=[2,3,4,5,6,7,8]
# m=map(sq,L1)    #m is the map object and this is also an iterator
# print(m)
# for e in m:
#     print(e)

# #New Program
# L1=[2,3,4,5,6,7,8]
# m=map(lambda a:a**2,L1)    #m is the map object and this is also an iterator
# print(m)
# L=list(m)
# print(L)

# #New Program
# L1=[2,3,4,5,6,7,8]
# L2=list(map(lambda a:a**2,L1))
# print(L2)

# #New Program
# L1=["Ahmedabad","Aurangabad","Surat","Agra","Aligarh","Faridabad"]
# L2=list(map(lambda s:s[0]=="A",L1))
# print(L2)

# #New Program
# print(2%2==0)
# """Filter Function: To filter out the selected elements
# of an iterator"""
# L1=[2,3,4,5,6,7,8]
# f=filter(lambda a:a%2==0,L1)
# print(f)
# print(list(f))

#New Program
# print(2%2==0)
#New Program

"""Filter Function: To filter out the selected elements
of an iterator"""
# #New Program
# L1=[2,3,4,5,6,7,8]
# f=map(lambda a:a**2,filter(lambda a:a%2==0,L1))
# print(f)
# print(list(f))

"""
Aanchal
Neha
Vinay
Pratyush
Rohan
Chinmay
Amit
Prashu
Syed Kareem
Khushi
Sanjay
Pawan
Nitin
Anshika
Asim Dahiya
Rahul
"""

"""
List Comprehension: Result will be a list only
list_var=[expression_as_element for_e_in_iterator condition]
here we have 3 arguments
1. expression_as_element 
2. for_e_in_iterator 
3. condition: Optional
"""
# #New Program
# L1=[2,3,4,5,6,7,8]
# L2=[e**2 for e in L1]
# print(L2)

# #New Program
# L1=[2,3,4,5,6,7,8]
# L2=[e**2 for e in L1 if(e%2==0)]
# print(L2)

# #New Program
# t1=(2,3,4,5,6,7,8)
# L2=[e**2 for e in t1 if(e%2==0)]
# print(L2)

#New Program
"""

"""
# L1=["Ahmedabad","Aligarh","Amritsar","Delhi","Meerut","Agra"]
# f=list(filter(lambda s:s[0]=="A",L1))
# print(f)


# # New Program
# L1=["Ahmedabad","Aligarh","Amritsar","Delhi","Meerut","Agra"]
# L2=[e for e in L1 if(e[0]=="A")]
# print(L2)

# #New Program
# L1=[2,5.5,"CETPA",6.75,8.23,"hello",True,9]
# L2=[e**3 for e in L1 if(type(e)==int)]
# print(L2)

# #New Program
# L1=[2,5.5,"CETPA",6.75,8.23,"hello",True,9]
# L2=[e**3 for e in L1 if(type(e)==int or type(e)==float)]
# print(L2)

#New Program
