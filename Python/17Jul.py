""
"""
Tuple: Collection of heterogeneous data types
var=(Comma separated elements)
"""
# t=(10,20,30,30.5,True,[2,3,4],"CETPA",(1,2))
# print(t)
# print(type(t))

# #New Program
# t=(10,20,30,20)
# print(t[2])
# i=t.index(20)
# print(i)
#
# #New Program
# t=(10,20,30,20)
# c=t.count(20)
# print(c)

"""
Dictionary: Collection of heterogeneous data type ie key-value pairs
dict_var={key1:value1,key2:value2,key3:value3}

Element access: dict_var[key]

We can easily access the data using dictionary
Data access is very fast in case of dictionary. In case of dictionary data is store
using hash maps ie hashing concepts. In actual dictionary keys represents hash
keys

Dictionary keys are always unique values, duplicate keys are not allowed
"""
# d={5:"CETPA","ABC":99.5,23.5:[2,3,4]}
# print(d)
# print(type(d))
# print(d[5])
# print(d["ABC"])

# #New Program
# cus_dict={10:["Vikas",39],20:["Anil",41],30:["Amit",45]}
# print(cus_dict[30])
# print(cus_dict[30][0])
# print(cus_dict[30][1])
# id=int(input("Enter Customer ID:"))  #id=20
# print("Cust ID:",id,"Cust Name:",cus_dict[id][0],"Cust Age:",cus_dict[id][1])

# #New Program
# d={1:20,2:30,3:30,4:40,3:50}
# print(len(d))
# print(d)

# #New Program
# d={}
# id=10
# name="Vikas"
# age=39
# d[id]=[name,age]
# print(d)

"""Dictionary is mutable in nature ie if we change the elements of dictionary 
then new dictionary won't be created"""

# #New Program
# d={1:10,2:20,3:30}
# print(id(d))
# d.clear()
# print(id(d))
# print(d)

# #New Program
# d={1:10,2:20,3:30}
# print(id(d))
# d[2]=90
# print(id(d))
# print(d)

# #New Program
# d={1:10,2:20,3:30}
# r=d.pop(2)
# print(d)
# print(r)

# #New Program
# d1={1:10,2:20,3:30}
# print(id(d1))
# d2=d1.copy()
# print(id(d2))
# print(d2)

# #New Program
# d={1:10,2:20,3:30}
# print(d.get(2))
# print(d[2])

# #New Program
# d={1:10,2:20,3:30}
# k=d.keys()    #Return all keys of dictionary
# print(k)
# print(type(k))   #<class 'dict_keys'>, indexing not supported on this

# #New Program
# d={1:10,2:20,3:30}
# k=d.keys()    #Return all keys of dictionary
# print(k[0])  #Error

# #New Program
# d={1:10,2:20,3:30}
# k=d.values()    #Return all keys of dictionary
# print(k)
# print(type(k))   #<class 'dict_keys'>, indexing not supported on this

# #New Program
# d={1:10,2:20,3:30}
# k=d.items()    #Return all keys of dictionary
# print(k)
# print(type(k))   #<class 'dict_keys'>, indexing not supported on this

# #New Proggram
# d={1:10,2:20,3:30}
# for e in d:
#     print(e,d[e])

#New Program
# d={1:10,2:20,3:30}
# for e in d:
#     print(e)
# for e in d.keys():
#     print(e)
# for e in d.values():
#     print(e)
# for e in d.items():
#     print(e,e[0],e[1])

# #New Program
# d={1:10,2:20,3:30}
# r=d.popitem()
# print(d)
# print(r)

"""update method and setdefault method: Using both the methods, we can add
new items (key-value) pairs in dictionary. In update method, to add elements
we need to pass a dictionary only so using update method we can add one or
more items in dictionary. In setdefault method, we need to pass two different
arguments, first argument will be key and second argument will be value. Using
setdefault method max only 1 item at a time. In update method, if we are trying
to add key-value pair where key already exists in dictionary then value of that
key will be updated. But in setdefault method, if we are trying
to add key-value pair where key already exists in dictionary then value of that
key will won't be updated"""

# #New Program
# d={1:10,2:20,3:30}
# d.update({5:50,2:60})
# print(d)
# #New Program
# d={1:10,2:20,3:30}
# d.setdefault(2,60)
# print(d)
# #New Program
# d={1:10,2:20,3:30}
# d.setdefault(5,50)
# print(d)

# #New Program
# d={1:10,2:20,3:30}
# d.setdefault({2:50})    #Error
# print(d)

"""
Assignment: Update CMS using Dictionary
"""

"""
Write a Python program to find the sum of keys and values of a dictionary. 
All keys and values are of int type.
"""
# d={1: 10, 2: 60, 3: 30, 5: 50}
# r1=0
# r2=0
# for e in d:         #e=1,2,3,5, d[e]: 10,60,30,50
#     r1=r1 + e
#     r2=r2 + d[e]
# print(r1,r2)

# #New Program
# d={1: 10, 2: 60, 3: 30, 5: 50}
# r1=0
# r2=0
# for e in d.items():         #e=(1,10), (2,60).....
#     r1=r1 + e[0]
#     r2=r2 + e[1]
# print(r1,r2)

"""
Formatted String:
"""
# n="Vikas"
# a=39
# print("Cust name is n and age is a years")
# print("Cust Name is",n,"and his age is",a,"Years")
# print("Cust name is {n} and age is {a} years")
# print(f"Cust name is {n} and age is {a} years")
# print("Cust name is {name} and age is {age} years".format(name=n,age=a))

"""
set and frozenset are collection of heterogeneous data type:
set is mutable
frozenset is immutable

Difference between set and list: set can hold only unique values. Set values
in the background are saved like hash keys.

set_var={comma separated values}
frozenset_var=frozenset(source_var)     #Through type casting
"""
# s={10,20,30,40,40.5,30}
# print(s)
# print(len(s))

# #New Program:To remove duplicate values from a list
# L=[10,20,30,30,40,45,30,20,10,90,80,80]
# s=set(L)
# print(s)
# L=list(s)
# print(L)

# #New Program
# s={10,20,30}
# print(s,type(s))
# f=frozenset(s)
# print(f,type(f))

# #New Program
# s1={10,20,30,40,50}
# s2={40,50,60,70,80}
# r1=s1.union(s2)
# r2=s1.intersection(s2)
# print(r1)
# print(r2)

#New Program
