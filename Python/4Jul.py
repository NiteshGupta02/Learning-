""
"""
Python is a case sensitive language
Data Types: What kind of values can be there
Single Element:
int: 23, 45
float: 4.0, 6.78
complex: 2+3j
bool: True, False


Multi Element: Iterators
str: 
list
tuple
dict
set
frozenset
"""
# #New Program
# s="CETPA"
# print(s)
# print(type(s))

"""
String: Is a collection of homogeneous data types ie characters only. 

List is a collection of heterogeneous data types.
list_var=[Comma separated elements]

There is no negative marking in our class.
No Practise No Learning

"""

# #New Program
# L1=[23,44.5,"cetpa",True]
# print(L1)
# print(type(L1))

"""
Indexing and Slicing: MultiElement Data Types: Iterators
Indexing: Accessing Individual element of iterator
s="Welcome"  : Indices will vary from 0 to n-1 ie 6, n=7
Indexing Syntax: var[index]

Slicing: Accessing multiple elements
Basic Syntax: var[lower_bound:upper_bound] and upper bound is discarded in slicing or at most
of the places in Python

"""
# #New Program
# s="Welcome"
# print(s[0])
# print(s[1])
# print(s[5])
# print(s[6])

# #New Program
# s="Welcome"
# print(s[0:3])       #s[0]s[1]s[2]

# #New Program
# s="Welcome"
# print(s[2:6])

# #New Program
# L=[10,20,30,40,50,60,70,80]     #Indices 0 to 7
# print(L[0])
# print(L[5])
# print(L[1:6])

"""
Slicing: 
Complete Syntax: var[lower_bound:upper_bound:step_size]
Step Size is optional: Default step size is 1 

There is no negative marking in our session

+ve Index: 0 to n-1 where 0 is index of left most element and n-1 is index of right most element
-ve Index: -1 to -n where -1 is index of right most element and -n is index of left most element

In case of indexing: If index passed is out of range then IndexError will be generated

In case of slicing: If index passed is out of range then there won't be any error

In case of +ve step size: Upper bound should be bigger than lower bound
In case of -ve step size: Upper bound should be smaller than lower bound
"""
#New Program
# s="Welcome"
# print(s[2:6])
# print(s[2:6:1])     #s[2]s[3]s[4]s[5]

# #New Program
# s="Welcome"
# print(s[2:6:2])     #s[2]s[4]

# #New Program
# s=[10,20,30,40,50,60,70,80]
# print(s[0:7:3])     #s[0]s[3]s[6]

# #New Program
# s="Welcome" #n=7, 0 to 6 or -1 to -7
# print(s[0])
# print(s[-7])
# print(s[6])
# print(s[-1])

# #New Program
# s="Welcome" #0 to 6
# print(s[6:2:-1])        #s[6]s[5]s[4]s[3]

# #New Program
# s="Welcome"     #s indices 0 to 6
# print(s[10])    #IndexError: string index out of range

# #New Program
# s="ab cd"   #0 to 4
# print(len(s))

# #New Program
# s="Welcome"
# print(s[4:10])

# #New Program
# s="Welcome"
# print(s[10:20])

# #New Program
# s=[10,20,30]    #index 0 to 2
# print(s[10:20])

# #New Program
# s="Welcome"
# print(s[5:2:-1])        #moc
# print(s[5:2:1])     #s[5:2] #Empty String
# print(s[5:5:1])     #Empty String
# print(s[2:5:1])     #lco

# #New Program
# L=[10,20,30,40,50,60,70]
# print(L[2:6:2])
# print(L[-2:-6:2])
# print(L[6:2:2])
# print(L[2:6:-2])
# print(L[-2:-6:-2])  #s[-2]s[-4]
# print(L[6:2:-2])    #s[6]s[4]

# #New Program
# L=[10,20,30,40,50,60,70,80,90]      #0 to 8
# print(L[-7:-1:-3])
# print(L[-1:-7:-3])
# print(L[-1:-20:-3])         #L[-1]L[-4]L[-7]

"""
Default step size is 1

For +ve Step Size: Default lower bound is 0 and Default upper bound is n
For -ve Step Size: Default lower bound is -1 and Default upper bound is -n-1


"""
# #New Program
# s="Welcome" #n=7, indices 0 to 6
# print(s[::2])       #s[0]s[2]s[4]s[6], upper bound 7 will be discarded

# #New Program
# s="Welcome" #n=7, indices 0 to 6, -1 to -7
# print(s[::-2])       #s[-1]s[-3]s[-5]s[-7], upper bound -8, s[-1:-8:-2]

# """Question asked in MNC's: Reverse a String without using any method or loops"""
# #New Program
# s="Welcome"     #0 to 6
# print(s[::1])   #s[0:7:1]
# print(s[::-1])  #s[-1:-8:-1]

# #New Program
# s="Welcome"
# print(s)
# print(s[:])       #s[0:7]
# print(s[::])      #s[0:7:1]
# print(s[::1])      #s[0:7:1]
# print(s[0:7:1])

"""If Lower and Upper bounds are of different signs then firstly convert them into common signs
preferably for +step size convert to +bound and -ve step size convert to -ve bounds"""
# #New Program
# s="Welcome"
# print(s[-1:3:-1])       #s[-1:-4:-1]

"""
Escape Characters: \
#\t
\n
\b
"""
# print("C\t\t\tE\tTPA")
# print("C\n\n\nE\tTPA")
# print("CET\bPA")

# #New Program
# print("CET\b\bPA")      #CPA
#
# #New Program


# #New Program
# s="CETPA INFOTECH"
# print(s.count("T"))
# print(s.lower())

# #New Program
# L=["AB", "CD"]
# print(L.lower())    #AttributeError: 'list' object has no attribute 'lower'

"""Syntax to call a function
Function_Name(Arguments)

Method: Generally the functions defined inside class are called methods
Syntax to call a method
var_name.method_name(arguments)
"""
# s="CETPA"
# print(type(s))

# #New Program
# s="Cetpa Infotech"
# print(s.swapcase())

# #New Program
# s="CETPA INFOTECH"
# print(s.count("INFO"))
# print(s.count("W"))

