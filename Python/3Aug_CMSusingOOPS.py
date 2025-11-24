""
"""CMS using OOPS with Exception handling"""
#BLL
import pickle
import pymysql
from tkinter import *
from tkinter import messagebox
class Customer:
    con=pymysql.connect(host="127.0.0.1",user="root",password="vikaskalra",database="db1")
    cur=con.cursor()
    cuslist=[]      #Static Variable
    def __init__(self): #self=1000
        self.id=0
        self.name = 0
        self.age=0
        self.mob = 0
    def addCustomer(self):  #self=1000, self=2000
        for cus in Customer.cuslist:
            if(cus.id==self.id):
                raise ValueError("Duplicate ID")
        Customer.cuslist.append(self)       #cuslist=[1000,2000,3000....
        Customer.cur.execute(f"insert into custable values({self.id},{self.age},'{self.name}',{self.mob})")
        Customer.con.commit()
    def searchCustomer(self):   #self=9000, self.id=20, self.name=0....
        qry=f"select * from custable where id={self.id}"
        Customer.cur.execute(qry)
        cusdata=Customer.cur.fetchone()
        return cusdata

        # print(cusdata)
        # Customer.cur.execute(qry)
        # cusdata=Customer.cur.fetchall()
        # print(cusdata)

        # for e in Customer.cuslist:  #e=1000
        #     if(e.id==self.id):
        #         self.name=e.name    #self.name="Anil"
        #         self.age=e.age      #self.age=41
        #         self.mob=e.mob
        #         break       #return
        # else:
        #     raise ValueError("ID not Found")
    def deleteCustomer(self):   #self=10000, self.id=30
        # for e in Customer.cuslist:
        #     if(e.id==self.id):
        #         Customer.cuslist.remove(e)
        #Another Way
        for i in range(len(Customer.cuslist)):      #i=0,1,2
            if(self.id==Customer.cuslist[i].id):
                Customer.cuslist.pop(i)
                return
    @staticmethod
    def deleteCustomerStatic(id):       #id=30
        qry=f"delete from custable where id={id}"
        Customer.cur.execute(qry)
        Customer.con.commit()

        # for i in range(len(Customer.cuslist)):      #i=0,1,2
        #     if(id==Customer.cuslist[i].id):
        #         Customer.cuslist.pop(i)
        #         return  #break
        # else:
        #     raise ValueError("ID not Found")

    def modifyCustomer(self):       #self=11000, self.id=20,self.name="Banti"...
        for e in Customer.cuslist:  #e=1000
            if(e.id==self.id):
                e.name=self.name
                e.age=self.age
                e.mob=self.mob
    @staticmethod
    def dumptoPickle():
        f=open("D:/vikas/cmsdata.txt","wb")
        pickle.dump(Customer.cuslist,f)
        f.close()

    @staticmethod
    def loadfromPickle():
        f = open("D:/vikas/cmsdata.txt", "rb")
        Customer.cuslist=pickle.load(f)
        f.close()

    @staticmethod
    def loadDatafromDatabase():
        qry="select * from custable"
        Customer.cur.execute(qry)
        data=Customer.cur.fetchall()
        return data
# print("Welcome to Rahul's CMS")

def getAge():
    while(1):
        age=input("Enter Cust Age:")
        if(age.isdecimal()):
            age=int(age)
            if(age>=10 and age<=110):
                return age
            else:
                print("Incorrect Age, Enter age between 10 to 110 only")
        else:
            print("Enter Age in Numbers Only")

def getMob():
    while(1):
        mob=input("Enter Mobile No:")
        if(len(mob)==10 and mob.isdecimal()):
            return mob
        else:
            print("Enter Mob No in Correct Format Only")

#PL
def addButtonClick():
    cus=Customer()
    cus.id=var_id.get()
    cus.name=var_name.get()
    cus.age=var_age.get()
    cus.mob=var_mob.get()
    cus.addCustomer()
    messagebox.showinfo("Cust Added",message="Customer Added Successfully")
    var_id.set("")
    var_name.set("")
    var_age.set("")
    var_mob.set("")
def searchButtonClick():
    cus=Customer()      #9000
    cus.id=var_id.get()
    data=cus.searchCustomer()
    # print(data)
    var_age.set(data[1])
    var_name.set(data[2])
    var_mob.set(data[3])
def displayAllButtonClick():
    global root1
    root1=Tk()
    data=Customer.loadDatafromDatabase()
    # print(data)
    lblid_heading=Label(root1,text="CUST ID",font=20,bg="Yellow",width=20)
    lblid_heading.grid(row=0,column=0)
    lblname_heading = Label(root1, text="CUST NAME", font=20, bg="Yellow", width=20)
    lblname_heading.grid(row=0, column=1)
    lblage_heading = Label(root1, text="CUST AGE", font=20, bg="Yellow", width=20)
    lblage_heading.grid(row=0, column=2)
    lblmob_heading = Label(root1, text="CUST MOB", font=20, bg="Yellow", width=20)
    lblmob_heading.grid(row=0, column=3)
    for i in range(len(data)):
        lbl_id1=Label(root1,text=data[i][0],font=20,bg="Orange",width=20)
        lbl_id1.grid(row=i+1,column=0)
        lbl_name1 = Label(root1, text=data[i][2], font=20, bg="Orange", width=20)
        lbl_name1.grid(row=i + 1, column=1)
        lbl_age1 = Label(root1, text=data[i][1], font=20, bg="Orange", width=20)
        lbl_age1.grid(row=i + 1, column=2)
        lbl_mob1 = Label(root1, text=data[i][3], font=20, bg="Orange", width=20)
        lbl_mob1.grid(row=i + 1, column=3)
def exitButtonClick():
    root.destroy()
    try:
        root1.destroy()
    except:
        pass
root=Tk()
root.geometry("600x600")

lbl_id=Label(root,text="Cust Id: ",font=20)
lbl_id.grid(row=0,column=0)
var_id=StringVar()
entr_id=Entry(root,font=20,textvariable=var_id)
entr_id.grid(row=0,column=1)

lbl_name=Label(root,text="Cust Name: ",font=20)
lbl_name.grid(row=1,column=0)
var_name=StringVar()
entr_name=Entry(root,font=20,textvariable=var_name)
entr_name.grid(row=1,column=1)

lbl_age=Label(root,text="Cust Age: ",font=20)
lbl_age.grid(row=2,column=0)
var_age=StringVar()
entr_age=Entry(root,font=20,textvariable=var_age)
entr_age.grid(row=2,column=1)

lbl_mob=Label(root,text="Cust Mob: ",font=20)
lbl_mob.grid(row=3,column=0)
var_mob=StringVar()
entr_mob=Entry(root,font=20,textvariable=var_mob)
entr_mob.grid(row=3,column=1)
btn_add=Button(root,text="Add Cust",font=20,width=15,command=addButtonClick)
btn_add.grid(row=4,column=0)
btn_search=Button(root,text="Search Cust",font=20,width=15,command=searchButtonClick)
btn_search.grid(row=4,column=1)
btn_delete=Button(root,text="Delete Cust",font=20,width=15)
btn_delete.grid(row=4,column=2)
btn_modify=Button(root,text="Modify Cust",font=20,width=15)
btn_modify.grid(row=5,column=0)
btn_displayAll=Button(root,text="Display All",font=20,width=15,command=displayAllButtonClick)
btn_displayAll.grid(row=5,column=1)
btn_exit=Button(root,text="Exit",font=20,width=15,command=exitButtonClick)
btn_exit.grid(row=5,column=2)

root.mainloop()



# def showCustomer(e):        #e=1000
#     print("Cust ID:",e.id,"Cust Name:",e.name,"Cust Age:",e.age,"Cust Mob:",e.mob)
# def showCustomerfromData(cusdata):
#     print("Cust ID:", cusdata[0], "Cust Name:", cusdata[2], "Cust Age:", cusdata[1], "Cust Mob:", cusdata[3])
# while(1):
#     cus=Customer() #cus=1000, 4 instance variables will be created, cus=9000
#     choice=input("""Enter Choice: 1 Add Cust, 2 Search, 3 Delete, 4 Modify, 5 Display All,
#     6 Exit:, 7 Write In Pickle, 8 Load from Pickle: """)
#     if(choice=="1"):    #Add Customer
#         try:
#             cus.id=input("Enter Customer Id:")          #cus.id=10
#             cus.name=input("Enter Customer Name:")      #cus.name="vikas"
#             cus.age=getAge()
#             cus.mob=input("Enter Customer Mob:")             #getMob()        #cus.mob=123
#             cus.addCustomer()
#             print("Customer Added Successfully")
#         except Exception as err:
#             print("Error!",err)
#     elif(choice=="5"):  #Display All
#         data=Customer.loadDatafromDatabase()
#         for e in data:
#             showCustomerfromData(e)
#
#         # for e in Customer.cuslist:  #e=1000
#         #     showCustomer(e)
#     elif(choice=="2"):   #Search Cust, cus address 9000, cus.id=0,cus.name=0,cus.age=0,cus.mob=0
#         try:
#             cus.id=input("Enter Cust ID:")  #cus.id=20, 9000.id=20
#             cusdata=cus.searchCustomer()
#             showCustomerfromData(cusdata)
#
#             # showCustomer(cus)
#         except Exception as err:
#             print("Error!",err)
#     elif(choice=="3"):   #Delete Cust, cus=10000
#         try:
#             # cus.id=input("Enter Cust ID:")  #cus.id=30, 10000.id=30, 10000.name=0.....
#             # cus.deleteCustomer()    #cus=10000
#             id=input("Enter Customer ID:")  #id=
#             Customer.deleteCustomerStatic(id)
#             print("Customer Deleted Successfully")
#         except Exception as err:
#             print("Error",err)
#     elif(choice=="4"):  #Modify Cust, cus=11000, cus.id=0,cus.name=0....
#         try:
#             cus.id=input("Enter Cust Id to Modify Cust:")   #cus.id=20
#             cus.name=input("Enter Cust Updated Name:")      #cus.name="Banti"
#             cus.age = input("Enter Cust Updated Age:")      #cus.age=42
#             cus.mob = input("Enter Cust Updated Mob:")      #cus.mob=9212468020
#             cus.modifyCustomer()
#             print("Customer Modified Successfully")
#         except Exception as err:
#             print("Error!",err)
#     elif(choice=="6"):
#         print("Thanks for using Rahul's CMS")
#         Customer.con.close()
#         break
#     elif(choice=="7"):  #Save data in Pickle Format
#         Customer.dumptoPickle()
#         print("Data Saved to Pickle Format Successfully")
#     elif (choice == "8"):  # Load Data from Pickle Format
#         Customer.loadfromPickle()
#         print("Data Retrieved from Pickle Format Successfully")
#     else:
#         print("Incorrect Choice")


