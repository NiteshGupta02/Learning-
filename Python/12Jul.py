""
"""
Python:


"""
# s=input("Enter Few Numbers:")
# print(s)
# L=s.split()
# print(L)    #L= ['10', '20', '30', '40', '50']
# # count=0
# i=0
# while(L[i:i+1]!=[]):
#     i+=1
# print(i)

"""

Prime Number: 23

*
**
***
****
*****

Nested Loops
    *
   **
  ***
 ****
*****
n=5
i   j_max   k_max
0   4       1
1   3       2
2   2       3
3   1       4
4   0       5
j_max=n-i-1
k_max=i+1
"""
# #New Program
# n=int(input("Enter No of Lines:"))  #n=5
# i=0
# while(i<n):
#     j=0
#     while(j<n-i-1):     #4
#         print(" ",end="")
#         j+=1
#     k=0
#     while(k<i+1):
#         print("*",end="")
#         k+=1
#     print()
#     i+=1

"""
*        *
**      **
***    ***
****  ****
**********
j=i+1
k=2*(n-i-1)
l=i+1
"""

"""for Loop
1. using range
2. without using range

Membership Operators
in
not in
"""
# s="CETPA"
# print("T" in s)
# print("T" not in s)

"""
Syntax of for loop ie equivalent to while loop

for index in range(lower_bound,upper_bound,step size):
    Set of Statements
"""
# i=0
# while(i<5):
#     print("CETPA")
#     i+=1
# for i in range(5):     #range(0,5,1), i=0,1,2,3,4
#     print("HELLO")

# #New Program
# r=range(5)  #range is an iterator
# print(r)
# L=list(r)
# print(L)

# #New Program
# for i in range(2,21,2):
#     print(i)

# for i in range(5):     #range(0,5,1), i=0,1,2,3,4
#     print("HELLO")


# #New Programm
# s="CETPA"
# for i in s:
#     print(i)

"""
for index in range(lower_bound,upper_bound,step_size):
    set of statements
 1. in range iterator, if only two arguments are given, then
 third will be considered as step size and its default value 1
 2. in range iterator, if only one argument is given, then that
 argument will be upper bound, default lower bound =0, and 
 default step size=1
    
for element in iterator:
    set of statements
"""
# s="CETPA"
# i=0
# while(i<5):
#     print(s[i])
#     i+=1
#
# s="CETPA"
# for i in range(5):  #i=0,1,2,3,4
#     print(s[i])
#
# s="CETPA"
# for e in s:  #i=0,1,2,3,4 for i in iterator
#     print(e)


# #user defined len function
# s="CETPA*"
# count=0
# for e in s:
#     count+=1
# print(count)

# #New Program
# L=[10,20,30,40,50,60]
# for e in L:
#     print(e**2)

#New Program
"""
*
**
***
****
*****
"""
# for i in range(5):
#     for j in range(i+1):
#         print("*",end="")
#     print()

#New Program
"""break and continue keywords
To exit from the loop on some particular condition we can use
break keyword

To skip the set of statements inside loop for some particular
iterations, we can use loop
"""
# for i in range(5):
#     if(i==2):
#         break
#     print("CETPA")

"1sq,2sq,5sq,6sq,7qsq"
# #New Program
# for i in range(1,8):    #i=1,2,3,4,..7
#     if(i==3 or i==2):
#         continue
#     print(i**2)

# #New Program: res=1sq+4sq+5sq+6sq+7sq
# r=0
# for i in range(1,8):    #i=1,2,3,4,..7
#     if(i==3 or i==2):
#         continue
#     r=r + i**2
# print(r)

"""
We can use else with both the loops in Python. The else block only
runs when our loop is completely executed without break. In case
we break from the loop using break keyword then else block
won't run
"""
# #New Program: Prime Number
# n=int(input("Enter Any Number:"))   #n=15, 25, 11
# for i in range(2,n):    #i=2,3,4.....14
#     if (n%i==0):
#         print("Not a Prime No")
#         break
# else:
#     print("Prime No")


