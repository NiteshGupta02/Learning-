""
"""
For mysql Server Connectivity, we need to install an external package ie pymysql
To install an external package in pycharm:
First Option:
1. File menu
2. Setting
3. Interpreter
4. +icon click and 
5. Search Pymysql: install

Second Option:
1. Command prompt
2. pip install pymysql

To create a connection between Python and pymsysql server
1. IP Address: host
If python is installed in our computer along with mysql server is also installed in our computer
then we can access our computer from our computer with name as 'localhost' or our computer IP
address: 127.0.0.1
2. user='root'
3. password: 'vikaskalra'
4. database: 'db1'   (Can provide later)
5. In case there are multiple database servers or mysql servers are installed on your server then
we need to provide: port:...Optional
9711610401: Santosh Sir: Lab Admin CETPA
"""
# #New Program
# print("CE'T'PA")
# print('CE"T"PA')

# #New Program
# import pymysql
# con=pymysql.connect(host="localhost",user="root",password="vikaskalra",database="db1")
# print(type(con))    #con is an object of Connection class
# cur=con.cursor()
# print(type(cur))    #con is an object of Cursor class

"""If we are using DML instruction from outside database then after executing the instruction
we need to commit the connection"""
# #New Program
# import pymysql
# con=pymysql.connect(host="localhost",user="root",password="vikaskalra",database="db1")
# cur=con.cursor()
# qry="insert into cus values(10, 'vikas', 39, 123)"
# cur.execute(qry)
# con.commit()
# con.close()

# #New Program
# import pymysql
# con=pymysql.connect(host="localhost",user="root",password="vikaskalra",database="db1")
# cur=con.cursor()
# cur.execute("select * from cus")
# data=cur.fetchall()
# print(data)     #data will be retrieved in tuple of tuple forms
# for e in data:
#     print("Customer ID:",e[0],"Customer Name:",e[1],"Customer Age:",e[2],"Customer Mob:",e[3])
# con.close()


# #New Program
# import pymysql
# con=pymysql.connect(host="localhost",user="root",password="vikaskalra",database="db1")
# cur=con.cursor()
# qry="create table custable(id int, age int, name varchar(100), mob int)"
# cur.execute(qry)
# con.commit()
# con.close()

"""
Python padhne se job nahi milege: Python is a foundation course to enhance your skills into 
1. Data Driven Domains
2. Web Application Development Domains: Full Stack Developer:
"""

"There is no negative marking in our class"
#New Program
import pymysql
con=pymysql.connect(host="localhost",user="root",password="vikaskalra",database="db1")
cur=con.cursor()
id=40
name="vikas"
age=39
mob=1234
qry=f"insert into cus values({id},'{name}',{age},{mob})"
print(cur.mogrify(qry))
cur.execute(qry)
con.commit()
con.close()
