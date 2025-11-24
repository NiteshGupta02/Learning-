""
"""
Loops in Python
Loops are used to execute a block of code repeatedly.
There are two types of loops in Python: While and For

while Loop:
Syntax:

index Initialize (Variable initialize, from where to start)
while(condition):   (Condition, where to stop the loop)
    Indented set of statement
    increment/decrement index


"""
# i=0     #Initialize index
# while(i<5):     #Condition in while loop
#     print("CETPA")
#     print("Hello")
#     i+=1        #i=i+1  #i=1, 2, 3, 4, 5
# print("Out of Loop")


# #New Program
# i=1     #Initialize index
# while(i<=5):     #Condition in while loop
#     print("CETPA")
#     print("Hello")
#     i+=1        #i=i+1  #i=1, 2, 3, 4, 5
# print("Out of Loop")

# #New Program
# i=1     #Initialize index
# while(i<=5):     #Condition in while loop
#     print("CETPA")
#     print("Hello")
#                     #Infinte Loop
# print("Out of Loop")

# #New Program
# i=1     #Initialize index
# while(i>=5):     #Condition in while loop
#     print("CETPA")
#     print("Hello")
#     i=i+1                #i+=1
# print("Out of Loop")

"""
Assignment Operators:
=
+=
-=
*=
/=
%=
**=
//=     

a**=b means a = a** b


"""

# #New Program
# i=10
# while(i>=1):
#     print(i)
#     i-=1    #i=i-1, i=9, 8, 7,...........1, 0

"""
MAANG Companies
Meta
Amazon
Apple
Netflix
Google
"""

"""
If I want to run a loop for n times
i=0
while(i<n):
    Set of statement to run repeatedly
    i+=1
"""

#Table of 2 Print
"""
2
4
6
.
.
20

Create a Table
i       term(t)= 
0       2
1       4
2       6
3       8
.
.
9       20

Leave programming, now use your mathematics and tell
me relation between i and t ie if i is changing then
t should chhange, check how term(t) is dependent on i
t=(i+1)*2
"""
# #New Program
# i=0
# while(i<10):
#     t=(i+1)*2   #t=2, 4,...20
#     print(t)
#     i+=1        #i=1, 2,....10

"""
2
4
6
.
.
20

Create a Table
i       term(t)= 
1       2
2       4
3       6
4       8
.
.
10       20
t=i*2

"""
# #New Program
# i=1
# while(i<=10):
#     t=i*2
#     print(t)
#     i+=1

# #New Program
# i=2
# while(i<=20):
#     print(i)        #t=i
#     i+=2            #i=i+2
#
"""
s="CETPA"
i      term (t)
0       s[0]
1       s[1]
2       s[2]
3       s[3]
4       s[4]
t=s[i]

"""
# s="CETPA"
# i=0
# while(i<5):
#     print(s[i])
#     i+=1

# #New Program      #cntrl+/
# s=[10,20,30,40]     #indices 0 to 3
# i=0
# while(i<len(s)):    #len(s)=4, i = 0 to 3
#     print(s[i])     #s[0], s[1], s[2],s[3]
#     i+=1


# #New Program
# print("CETPA",end="")
# print("Hello",end="")
# print("Welcome",end="")

# #New Program
# print("CETPA",end="*$#")
# print("Hello",end="*$#")
# print("Welcome",end="")

# #New Program
# print("CETPA",end="  ")
# print("Hello",end="\t\t\t\t")
# print("Welcome",end="")

"*****"

"""
end is an optional parameter to pass in print. By default
end is having value "\n" due to which program moves to 
next line after print execution.
If we change end to a new value then that value is printed
at the end of print statements 
"""

# #New Program
# i=0
# while(i<5):
#     print("*",end="")
#     i+=1

# #New Program
# i=0
# while(i<5):
#     print()
#     i+=1

# #New Program
# i=0
# while(i<5):
#     print(end="*")
#     i+=1

"""
Level 1:
To print the indices or to print terms of an iterator.

Level 2:
To put some formula on index  or
to put some formula on elements of an iterator

to print the elements of a series or modify the elements of
an iterator and print
"""

# """2**2, 5**3,  8**4, 11**5,  14**6
# i       t
# 0       2**2    = 4
# 1       5**3    = 125
# 2       8**4    = 4096
# 3       11**5
# 4       14**6
# t=    (  ((i+1)*3) - 1) ** (i+2)
#
#
# """
# i=0
# while(i<5):
#     t=(  ((i+1)*3) - 1) ** (i+2)
#     print(t)
#     i+=1


"""2**2, 5**3,  8**4, 11**5,  14**6 
i       t
1       2**2    = 4
2       5**3    = 125    
3       8**4    = 4096
4       11**5
5       14**6
t=    (  (i*3) - 1) ** (i+2)


"""
# i=1
# while(i<=5):
#     t=(  ((i+1)*3) - 1) ** (i+2)
#     print(t)
#     i+=1

"""2**2, 5**3,  8**4, 11**5,  14**6 
i   j     t
2   2    2**2    = 4
3   5    5**3    = 125    
4   8    8**4    = 4096
5   11    11**5
6   14    14**6
t=    j**i


"""


# #New Program
# i=2
# j=2
# while(i<7):
#     print(j**i)
#     i+=1
#     j+=3

"""Loops are the heart of programming language, win that 
heart
"""

# #New Program
# i,j=0,0
# print(i<7 and j<8)

# #New Program
# L=[10,20,30,40,50]  #indices 0 to 4 ie 0 to len(L)-1
# i=0
# while(i<len(L)):    #i from 0 to 4
#     print(L[i])
#     i+=1

"""
Print the square of the elements of a list
"""
# L=[10,20,30,40,50]
# i=0
# while(i<len(L)):
#     t=L[i]**2
#     print(t)    #print(L[i]**2)
#     i+=1

#New Program (Sum elements at same index and print)
"""
110
220
330
440
550
"""
# L1=[10,20,30,40,50]         #indices 0 to 4
# L2=[100,200,300,400,500]    #indices 0 to 4
# i=0
# while(i<len(L1)):   #i= 0 to 4
#     t=L1[i]+L2[i]
#     print(t)    #L1[i]+L2[i]
#     i+=1

"""
How to generate the result of a string or an iterator
"""
# i=0
# while(i<5):
#     i = 0       #Infinte Loop
#     print(i)
#     i+=1

# #New Program
# i=0
# while(i<5):
#     i+=1
# print(i)      #Only last value will be printed

# #New Program
# s=input("Enter elements of list:")
# print(s)
# L=s.split()
# print(L)


# #New Program
# s="CE*TPA Info*tech P*vt. Ltd."
# print(s.split("*"))
# print(s.split())

# #New Program
# L=input("Enter elements of list:").split()
# print(L)