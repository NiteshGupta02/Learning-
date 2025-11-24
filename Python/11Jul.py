""
"""
Loops:

while Loop:


"""
# #New Program
# i=0
# while(i<5):
#     print("Welcome")
#     print("CETPA")
#     i+=1        #i=i+1

# #New Program: 2sq,4sq,6sq,.....20sq
# i=2
# while(i<=20):
#     print(i**2)
#     i+=2

# #New Program
# s="CETPA"
# i=0
# while(i<len(s)):
#     print(s[i])
#     i+=1


# #New Program: #Upper Function
# s="Cetpa* Info*tech"   #indices 0 to n-1, n elements
# i=0
# while(i<len(s)):    #i 0 to len(s)-1
#     t=ord(s[i])     #t=67, 101
#     if(t>=97 and t<=122):
#         t=t-32  #t=67, 69
#         t=chr(t)    #t="C","E"
#         print(t,end="")
#     else:
#         print(s[i],end="")
#     i+=1

#New Program


"""
Next Difficulty Level in Loops:
2sq+4sq+6sq+8sq+10sq+.....20sq

In most of the cases, if we have to perform some fixed
operation on elements on loop and then access the result
res=res operator term
where res should be initialize in such a way that when first
time loop runs, res should have the value of first term, 
initialize this value of res before loop starts


"""
# #New Program
# i=2
# r=0
# while(i<=20):
#     t=i**2  #t=2sq, 4sq, 6sq
#     r=r + t #r=2sq+4sq+6sq
#     i+=2
# print(r)

"""
L1=[10,20,30,40,50]
Cube the elements and multiply them and generate the result
res=10cube*20cube*....50cube
"""
# # New Program
# L1=[10,20,30,40,50] #L1[0],L1[1]...0,1,2,3,4
# i=0
# r=1
# while(i<len(L1)):   #while(i<5): i=0,1,2,3,4
#     t=L1[i]**3      #t=10cube, 20cube
#     r=r*t           #r=10cube, 10cube*20cube
#     i+=1
#     print(r)    #Don't write this statement
# print(r)

"""
Nested Loops: Loops inside Loop


i=0
while(i<5):
    Set of Statements
    i+=1

i=0
while(i<5): #Loop A
    j=0
    while(j<3): #New Program, i=0
        #Set of Statements
        j+=1    #j=1, j=2, j=3
    i+=1    #i=1

In case of nested loops with 1 loop inside other, then
if outer loop condition is to execute loop m times
and inner loop condition is to execute loop n times
then statements inside inner loop will run m*n times
ie everytime outer loop executes once then inner loop
executes n times  
"""
# i=0
# while(i<4):     #m=4
#     j=0
#     while(j<3): #n=3
#         print(i,j)  #i=0,j=0
#         j+=1        #i=0,j=1
#     i+=1


# #New Program
# L1=[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
# print(type(L1))
# print(type(L1[0]))
# print(L1[1][0])
# print(L1[2])
# u=L1[2]     #u=[7,8,9]
# print(u[0])
# print(L1[2][0])

# #New Program
# L=[[1,2,3],[4,5,6],[7,8,9],[10,11,12,13,14]]
# i=0
# while(i<len(L)):    #While(i<4): i= 0 to 3
#     j=0
#     while(j<len(L[i])):
#         print(L[i][j])
#         j+=1
#     i+=1

"""
Pattern Printing
*
**
***
****
*****
"""
# #New Program
# i=0
# while(i<5):
#     print("*")
#     i+=1

# #New Program
# i=0
# while(i<5):
#     print("*",end="")
#     i+=1

# #New Program
# i=0
# while(i<5):
#     print("*",end="")
#     i+=1
#     print()

# #New Program
# i=0
# while(i<5):
#     print("*")
#     i+=1
#     print()

# #New Program
# i=0
# while(i<4): #m=4
#     print("CETPA")
#     j=0
#     while(j<3): #n=3    #m*n times
#         print("Hello")
#         j+=1
#     print("Welcome")
#     i+=1

"""
Pattern Printing
*
**
***
****
*****
n=5
i   j max
0   1
1   2
2   3
3   4
4   5
Now find the equation for j dependent on i and n 
j_max=i+1

"""
# New Program
# i=0
# while(i<5):
#     j=0
#     while(j<i+1):
#         print("*",end="")
#         j+=1
#     print()
#     i+=1

# #New Program
# n=int(input("Enter No. of Lines:"))
# i=0
# while(i<n):
#     j=0
#     while(j<i+1):
#         print("*",end="")
#         j+=1
#     print()
#     i+=1

"""
*****
****
***
**
*
n=5
i   j_max
0   5
1   4
2   3
3   2
4   1
j_max=n-i
"""
#New Program
# n=5
# i=0
# while(i<n):
#     j=0
#     while(j<n-i):
#         print("*",end="")
#         j+=1
#     print()
#     i+=1