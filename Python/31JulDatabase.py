""
"""
Using Database in Python
Important Types of Database:
    1. Relational Database: SQL Database: Database is created using tables and 
    tables are connected on some common keys ie primary key...
    Examples: MySQL, Oracle, MS-SQL Server, MS-Access
    
    2. Non Relational Database : No SQL Database
    MongoDB, Cassendra Server....

SQL: Structured Query Language 

Database is used to store the data permanently and access the selected data at a very
fast speed

MySQL Installation:
1. Go to first link after searching mysql download
2. Click on 'MySQL Community (GPL) Downloads'
3. Click on Mysql community server
4. Download Windows (x86, 64-bit), MSI Installer	
5. Click on 'No thanks, just start my download.'
Now Mysql installer will be downloaded. 
Install First option ie typical version, install by clicking next, next, next
At the time of installation, it will ask to generate root user password.
my system sql server password: vikaskalra
Next, next it will be installed

Now to access mysql server in your computer:
search: mysql command line client: open

SQL Language: A language that is designed to work on all relational databases. 
    Multiple types of instructions:
        DDL: Data Definition Language
        DML: Data Manipulation/Modification Language
        DCL: Data Control Language
        DQL: Data Query Language
        .
        .
        .
        
Firstly to work on the database, we need to create the schema of the database and
queries/instructions to user are DDL..
Schema/DDL:
create database db1;
use db1;
create table tb1 (field_name:field_type,....);

CRUD: Create, Read, Update, Delete

DML: Data manipulation Language/Modification
insert into tb1(column_names) values (values);      Column name optional

DQL: Data Query Language:
select column_name from table_name;                * in place column_name, all columns will be selected
select * from tb1;
select * from tb1 where id=10;
select * from tb1 where id>10;

DML:
delete from tb1 where_clause;
delete from tb1 where id=10;
delete from tb1 where id<=20;

update tb1 set column_name=column_value where_clause;


 

Primary Key in particular field: Unique Key and can't have null value
Unique Key: Unique key but can have null value




"""