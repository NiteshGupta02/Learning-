""
"""
Python is a Platform Independent Language: CORA: Compile Once Run
Anywhere
You compile your code on one OS and execute it on any other OS
To convert a code to compiled code, firstly we need language compiler

So to run the compiled code on any OS, Virtual Machine (VM) should
already be there on that OS. So in case of Python this VM is called
PVM (Python Virtual Machine).
Java: JVM


Python supports Dynamic Data Type Definition and Dynamic Memory Allocation

How variables are made in Python: By assigning value to a variable
Whenever we assign a new value to a variable, a new variable is
created.
How memory is assigned to variables in Python:

Reference Counter: Is the count, which refers to the number
of variables referred to a particular memory location

In Python all variables are of reference type.
a=5 #Say 5 is stored at 1000 address and a is referring to 1000
b=a, address of a will be passed to b ie b will also start
referring to 1000 location

Whenever the value of ref counter goes 0 then automatically 
garbage collector process executes and that memory location is 
made free. 
"""
# a=5     #Variable of int type is created
# print(a)
# print(type(a))
# print(id(a))
# a="CETPA"
# print(a)
# print(type(a))
# print(id(a))

# #New Program
# a=49999
# b=49999
# print(id(a))
# print(id(b))

# #New Program
# a="cetpa"
# b="cetpa"
# print(id(a),id(b))

# #New Program
# a=[10,20,30]
# b=[10,20,30]
# print(id(a),id(b))

# #New Program
# a=5     #Say 5 is stored at 1000 location
# print(id(a))
# a=7     #Say 7 is stored at 2000 location
# print(id(a))

# #New Program
# a=5
# b=a
# print(id(a))
# print(id(b))

# #New Program
# a=[10,20,30]
# b=a
# print(id(a),id(b))

# #New Program
# a=5
# print(id(a))
# a=7
# print(id(a))
# a=10
# print(id(a))

"""
String vs List:
str: Collection of Characters:
str: Collection of homogeneous data type.

List: Collection of Heterogeneous data type

Data Type:
    Single element:
        int
        float
        complex
        bool
        NoneType
    Multi element: Iterators
        str
        list
        tuple
        dict
        set
        frozenset

list, dict and set, these are mutable data types
Rest all ie int, float, complex, bool, str, tuple, frozenset 
 are immutable
 
Mutable: Whose value can be changed. In actual, for mutable types,
we can make item assignment, ie we can change the elements of the
mutable types. If we change the elements then new variable won't
be created
Immutable: Whose value can't be changed, we can't change the 
elements.
 
"""
# a="CETPA"
# print(a,type(a))
# b=[10,23.5,"CETPA"]
# print(b,type(b))

# #New Program
# a="cetpa"
# a[0]="d"
# print(a)

# #New Program
# a="cetpa"
# print(a[0])
# print(a[1])

# #New Program
# L=[10,20,30]
# L[0]=40
# print(L)

# #New Program
# a="cetpa"
# print(a)
# a="hello"
# print(a)
# a=5
# print(a)
# a=7
# print(a)


# #New Program
# L=[10,20,30]
# print(L)
# print(id(L))
# L=[60,70,80]
# print(L)
# print(id(L))

# #New Program
# s="cetpa"
# s[0]="m"  #TypeError: 'str' object does not support item assignment

# #New Program
# L=[10,20,30]
# print(id(L))
# L[0]=40
# print(L,id(L))

"""
In Python variables are created by assigning values. Whenever we
assign a new value to a new variable\old variable, 
a new variable is created. But in case of mutable type variables
if we change the elements of variable then new variable won't be
created.
If we change the element of immutable type then error will be there

#In Following program we can't change value of 5 ie if 5 is
stored at 1000 location then we can't store 7 at this location
ie int is immutable type, but as we try to store 7 in a, then
it will be stored at a new location ie a new variable will be created.
"""
#New Program
# a=5
# print(id(a))
# a=7
# print(id(a))

#New Program: Replace C with R in following string
# s="CETPA"
# print(id(s))
# s=s.replace("C","R")
# print(id(s))
# print(s)

# #New Program
# s="CETPA"
# print(id(s))
# s="R"+s[1:]
# print(id(s))
# print(s)

# #New Program
# L=[10,20,30]
# print(id(L),L)
# L[0]=40
# print(id(L),L)
# L=[50,20,30]
# print(id(L),L)

"""
Functions in Python:
    User Defined (UDF)
    Pre Defined
    
What is a Function: A Function is a block of code, designed to
perform some specific task.

Why we use Functions:
1. Code Reusable
2. Dividing the code into different layers. Functions are the 
basic building block of layered architecture.
3. Functions are used to make the code scalable.
4. Functions are basic building block of modular approach of Programming
5. Reduce the complexity of code.


Scalable: Easily modifications possible
Layered Architecture: Dividing the code into multiple layers
Two most important layers of Programming are
1. Presentation Layer (PL): Presentation Layer is responsible for
user interaction. So in console we use, print and input function
and these functions are always used in PL.
2. Business Logic Layer (BLL): BLL is responsible for writing of 
the business logic.
Third layer is DLL (Data Link Layer) which comes into picture 
if we add some database in the Program

Modular Approach: We can divide our project into small modules and
finally all these modules can be interfaced together.

How to create a function:
Syntax:

def <function_name(parameters)>
    indented Block of statements
    return parameter (Optional)

How to call a function: Syntax
function_name(arguments)

No Learning No Practise
"""
