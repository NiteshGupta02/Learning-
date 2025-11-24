""
import re

"""
When to use static Methods: If we need object in method then we create
instance method, if we don't need object in method then we create
static method.

"""
# d={1:11,2:22,3:33,4:44}
# d1=d.pop(3)
# print(d)

# #New Program
# d={1:11,2:22,3:33,4:44}
# L=[10,11,12,13,14,15]
# r=d.fromkeys(L)
# print(r)

# #New Program
# L=[10,11,12,13,14,15]
# r=dict.fromkeys(L)
# print(r)


# #New Program
# class Customer:
#     @staticmethod
#     def addCustomer(self):
#         pass
#
# cus=Customer()
# Customer.addCustomer(cus)

"""
Regular Expression (RE/RegEx): is a tiny language, having few specific rules, which
is used to find strings or set of strings from other strings.
This language is supported by all different languages.
Only logics based language.
(RE is taught in automata subject in computer science stream)

To find the strings from other strings we create string patterns which
are created through meta characters.
Meta characters are special characters having special meaning in RE language


"""
#New Program
import re
s="""abc this is cetpa website contact us 9212468020, our overseas 
support number is 8800340007 query@cetpainfotech.com
vikaskalra@cetpainfotech.com,  abcd@gmail.com
"""
#To find contact numbers and email ids from a string
# p="\d{10}"
# phone=re.findall(p,s)
# print(phone)
# p="\w+@\w+\.\w+"
# email=re.findall(p,s)
# print(email)

"""
Library: re
result=re.findall(pattern,string)

Meta Characters:
^  $  .  *  +  ?  []  {}  ()  | \  
Rule 0.
To find any specific sub-string/character from a string, we can directly make a
pattern using that string. We can't search meta characters directly

Rule 1:
[] : Character Class: If we want to search any character from a group of
character then we can save that group inside character class. Even
we can search meta characters after writing in character class

Rule 2:
[a-zA-Z0-9_]: We can search alphanumeric characters by using \w
In place of using [a-zA-Z0-9_], we can also use \w
\w: Alphanumeric characters will be searched, generally w means word
\W: Non alphanumeric characters
[0-9] cac be replaced by \d: ie digit
\d:  [0-9]: All number characters
\D:  All non numbers characters
\s: All space related characters
\S: Non space characters

Rule 3: Quantity Class
{m,n}: All matching strings having length m to n characters will be searched
        Will try to make patterns of n characters, if not possible then
        n-1 characters, if not possible then n-2 characters and so on
        and finally will search min m characters and max n characters.
        
{m}: All matching strings of length m will be searched
{m,}: All matching strings of length m or more characters will be searched
{,n}: All matching strings of length 0 to n characters will be searched
Rule 4: Quantity Matcher Meta Characters

?: {,1}: 0 or 1 occurrence
+: {1,}:  1 or more occurrence
* : 0 or more occurrence

Rule 5: 
\ : Metacharacter
We can use \ along with a meta character to search a meta character
        ie \ will remove the special functionality of metacharacter
        like, I want to search . character then I can write [.] or \.

Rule 6:
. : Metacharacter, search all non new line characters

Rule 7:
|  : Metacharacter: Oring of patterns

Rule 8:
() : Search characters in brackets along with some other pattern, and other
pattern is removed

Rule 9:
^ : Metacharacter: Search starting of string
$: Metacharacter: Search end of string

"""
# import re
# s="Welcome to CETPA. CETPA is No 1 Training Company. I Love CETPA"
# p="CETPA"
# res=re.findall(p,s)
# print(res)
# print(len(res))

# #New Program
# import re
# s="Welcome ###to CETPA. CETPA is No 1 Training Company##. I Love CETPA"
# p="#"
# res=re.findall(p,s)
# print(res)

# #New Program
# import re
# s="Welcome ###to CETPA. CETPA is No 1 Training Company##."
# p="[amnpq]"
# res=re.findall(p,s)
# print(res)

#New Program
# import re
# s="Welcome ###to CETPA. CETPA is No 1 Training Company##."
# p="[a-e]"
# res=re.findall(p,s)
# print(res)

# #New Program
# import re
# s="Welcome ###to CETPA. **CETPA is No 1 Training Company##."
# p="[#.*]"
# res=re.findall(p,s)
# print(res)

# #New Program
# import re
# s="123 ###to** _CETPA_."
# p="[a-zA-Z0-9_]"        #Alphanumeric in RE
# res=re.findall(p,s)
# print(res)

# #New Program
# import re
# s="123 ###to** _CETPA_."
# p="[a-zA-Z0-9_]"        #Alphanumeric in RE
# res=re.findall(p,s)
# print(res)

# #New Program
# import re
# s="123 ###to** _CETPA_."
# p=r"\w"        #Alphanumeric in RE: p="[a-zA-Z0-9_]"
# res=re.findall(p,s)
# print(res)

# #New Program
# import re
# s="123 ###to** _CETP\tA_."
# p=r"\W"        #
# res=re.findall(p,s)
# print(res)


# #New Program
# import re
# s="123 ###to** 4  67_CETP\tA_."
# p=r"\d"        #
# res=re.findall(p,s)
# print(res)

# #New Program
# import re
# s="123 ###to** 4  67_CETP\tA_."
# p=r"\D"        #
# res=re.findall(p,s)
# print(res)

# #New Program
# import re
# s="123 ###t\no** 4  67_CETP\tA_."
# p=r"\s"        #
# res=re.findall(p,s)
# print(res)

# #New Program
# import re
# s="123 ###t\no** 4  67_CETP\tA_."
# p=r"\S"        #
# res=re.findall(p,s)
# print(res)

# #New Program
# import re
# s="Welcome to CETPA. Call us at 9212468020"
# p=r"\w{5,}"
# res=re.findall(p,s)
# print(res)

# #New Program
# import re
# s="Welcome to CETPA. Call us at 9212468020"
# p=r"\w{5,8}"
# res=re.findall(p,s)
# print(res)

# #New Program
# import re
# s="Welcome to CETPA. Call us at 9212468020"
# p=r"\w{,3}"
# res=re.findall(p,s)
# print(res)

# #New Program
# import re
# s="Welcome to CETPA. 45678Call us at 9212468020"
# p=r"\d{10}"
# res=re.findall(p,s)
# print(res)

# #New Program
# import re
# s="Welcome9897163434 to +92-8877665544CETPA. 45678Call us at +91-9212468020"
# p=r"[+]\d{2}-\d{10}"        #"cetpa"
# res=re.findall(p,s)
# print(res)

# #New Program
# import re
# s="Welcome+1-9897163434 to +92-8877665544CETPA. 45678Call us at +91-9212468020"
# p=r"[+]\d{1,2}-\d{10}"        #"cetpa"
# res=re.findall(p,s)
# print(res)

# #New Program: Search Email ID's
# import re
# s="abc@gmail.co vk@cetpa.com infy a@b.c:  pq_r@infy.com hello"
# p=r"\w{1,}@\w{1,}[.]\w{1,}"        #"cetpa"
# res=re.findall(p,s)
# print(res)

# #New Program: Search Email ID's
# import re
# s="abc@gmail.co vk@cetpa.com infy a@b.c:  pq_r@infy.com hello"
# p=r"\w+@\w+[.]\w+"        #"cetpa"
# res=re.findall(p,s)
# print(res)


# #New Program: Search Email ID's
# import re
# s="abc@gmail.co vk@cetpa.com infy a@b.c:  pq_r@infy.com hello"
# p=r"\w+@\w+[.]\w+"        #"cetpa"
# res=re.findall(p,s)
# print(res)

# # New Program:
# import re
# s="abcde abg123"
# p=r"[abcd]|[efg]"
# res=re.findall(p,s)
# print(res)

# # New Program:
# import re
# s="abcde abg123"
# p=r"(ab)cd"
# res=re.findall(p,s)
# print(res)


# # New Program:
# import re
# s="CETPA is no1 company. CETPA is Best. You should join CETPA"
# p=r"^CETPA"
# res=re.findall(p,s)
# print(res)

# # New Program:
# import re
# s="CETPA is no1 company. CETPA is Best. You should join CETPA"
# p=r"CETPA$"
# res=re.findall(p,s)
# print(res)

# # New Program:
# import re
# s="CETPA is no1 company. CETPA is Best. You should join CETPA"
# p=r"abcd$"
# res=re.findall(p,s)
# print(res)

# #New Program
# n=input("Enter Your Name:")
# print(len(n),n)
# n=n.strip()
# print(len(n),n)

# #New Program
# n=input("Enter Your Name:").strip()
# print(len(n),n)

# #New Program
# """Kailash Sir: Django Best Trainer"""

"""This was the end of Python Batch"""
