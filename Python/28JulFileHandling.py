""
"""

"""
# #New Program
# f=open("D://vikas/cetpa4.txt","rb")
# print(f.read(10))
# print(f.tell())
# f.seek(-5,1)
# print(f.tell())
# print(f.read(5))
# print(f.tell())

#New Program
"""


When we transfer data to one programming language to
another then data is transferred in some standard formats.
1. Most Popular format is JSON
2. Then XML
.

Python to Python Data Transfer: Standard: Pickle 

To transfer data : 
Serialization: To convert your data into some standard objects
Deserialization: To convert standard object data to python data/
                programming data

Pickling: Standard Python partially encrypted format which
works on binary format to transfer the data
"""
# #New Program
# import pickle
# L1=[23,45.6,"ABC"]
# f=open("D://vikas/cetpa6.txt","wb")
# pickle.dump(L1,f)
# f.close()

# #New Program
# import pickle
# f=open("D://vikas/cetpa6.txt","rb")
# L=pickle.load(f)
# print(L)
# f.close()


