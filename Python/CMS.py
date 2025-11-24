""
"""
First Project of Python Programming ie CMS

Customer Management System:
Few Operations say
Add Customer
Search Customer
Delete Customer
Modify Customer
Display All Customer
 
"""
#BLL
def addCustomer(id,name,age,mob):   #10, Vikas, 39, 9212468020
    idlist.append(id)
    namelist.append(name)
    agelist.append(age)
    moblist.append(mob)
def searchCustomer(id):  #id=20
    index=idlist.index(id)
    return index
def deleteCustomer(id): #id=20
    index=idlist.index(id)  #index=1
    idlist.pop(index)
    namelist.pop(index)
    agelist.pop(index)
    moblist.pop(index)
def modifyCustomer(id,name,age,mob):    #id=20, name="Prashant"...
    index=idlist.index(id)  #index=1
    namelist[index]=name
    agelist[index]=age
    moblist[index]=mob

#PL
print("Welcome to Suhail's CMS")
idlist=[]       #idlist=['10','20','30']
namelist=[]     #namelist=["Vikas","Anil","Amit"]
agelist=[]      #agelist=['39','41',45]
moblist=[]      #moblist=['9212468020','9654444252','9897156427']
def showCustomer(i):    #i=1
    print("Cust ID:",idlist[i],"Cust Name:",namelist[i],"Cust Age:",agelist[i],"Cust Mob:",moblist[i],)
while(1):
    ch=input("Enter Choice, 1 Add Cust, 2 Search Cust, 3 Delete Cust, 4 Modify, 5 Display All, 6 Exit: ")
    if(ch=="1"):        #Add Customer
        id=input("Enter Cust Id:")  #10
        name = input("Enter Cust Name:")    #'Vikas'
        age = input("Enter Cust Age:")      #39
        mob = input("Enter Cust Mob:")      #9212468020
        addCustomer(id,name,age,mob)
        print("Customer Added Successfully")
    elif(ch=="2"): #Search Customer
        id=input("Enter Cust Id to Search Cust:")   #20
        i=searchCustomer(id)        #i=1
        showCustomer(i)
    elif(ch=="3"):  #Delete Customer
        id = input("Enter Cust Id to Delete Cust:")  # 20
        deleteCustomer(id)
        print("Customer Deleted Successfully")
    elif(ch=="4"): #Modify Customer
        id=input("Enter Customer ID to Modify Cust:")   #id=20
        name=input("Enter Cust Updated Name:")  #name="Prashant"
        age=input("Enter Cust Updated Age:")    #age=46
        mob=input("Enter Cust Updated Mob:")    #mob=8877665544
        modifyCustomer(id,name,age,mob)
        print("Customer Modified Successfully")
    elif(ch=="5"):  #Display All
        for i in range(len(idlist)):
            showCustomer(i)
    else:
        print("Thanks for using Suhail's CMS")
        break



