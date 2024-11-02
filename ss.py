import mysql.connector as sql
conn=sql.connect(host='localhost',user='root',passwd='password',database='shoebilling')
if conn.is_connected():
print('connected sucessfully')
conn.autocommit=True
c1=conn.cursor()
c1.execute("create table shoe_details(shoe_code int primary key,brand_name varchar(25),customer_name varchar(25),customer_number int,customer_address varchar(25),amount int )")
c1.execute("create table shoe_collection(shoe_code int primary key,brand varchar(25),model varchar(10),price int)")
c1=conn.cursor()
def cust_details():
code=input("enter code=")
brand =input("enter brand=")
name=input("enter customer name=")
number=input("enter phone number=")
details=input ("adress=")
amount=input("amount=")
c1.execute("insert into shoe_details values ("+code+",'"+brand+"'"+",'"+name+"',"+number+",'"+details+"',"+amount+")")
conn.commit()
def show_details():
v_code=input("enter the code number")
c1.execute("select * from shoe_details where shoe_code ="+v_code)
data=c1.fetchone()
if data==None:
print("sorry no such number")
return
print("Shoe code:",data[0])
print("brand name:",data[1])
print("customer name:",data[2])
print("customer number:",data[3])
print("customer detail:",data[4])
print("amoumt:",data[5])
def new_collections():
scode=int(input('enter code'))
sbrand=input('enter brand')
smodel=input('enter model')
sprice=int(input('enter price'))
c1.execute("insert into shoe_collection values('{}','{}','{}',{})".format(scode,sbrand,smodel,sprice))
conn.commit()
c1.execute("select * from shoe_collection")
row=c1.fetchone()
while row is not None:
print(row)
row=c1.fetchone()
def search_shoe():
c=int(input('enter the code'))
c1.execute("select * from shoe_collection where shoe_code={}".format(c))
r=c1.fetchone()
if r==None:
print('code is not valid')
else :
for i in r:
print(i)
def modify_details():
f=int(input('enter the customer number'))
c1.execute("select * from shoe_details where customer_number={}".format(f))
r=c1.fetchone()
if r==None:
print("no such customer number")
return
c=int(input('enter choice; 1:name , 2:address'))
if c==1:
n=input('enter new name')
c1.execute("update shoe_details set customer_name='{}' where customer_number={}".format(n,f))
conn.commit()
else :
a=input('enter new address')
c1.execute("update shoe_details set customer_address='{}' where customer_number={}".format(a,f))
conn.commit()
def discount():
scode=int(input('enter code'))
c1.execute("select price from shoe_collection where shoe_code={}".format(scode))
r1=c1.fetchone()
if r1==None:
print('no code found')
return
print(r1)
k=int(r1[0])
print('the OG price is', k)
print('1 ramzan discount')
print('2 christmas discount')
print('3 diwali discount')
i=int(input('enter choice'))
if i==1:
r=k*50/100
elif i==2:
r=k*25/100
elif i==3:
r=k*20/100
print('price after discount is',k-r)
user=input("enter user")
passwd=input("enter password")
v='y'
if user=='messi' and passwd=='leo':
print(" shoe billing")
print(" ")
print("1:ENTER CUSTOMER DETAILS")
print(" ")
print("2:SHOW CUSTOMERS DETAILS")
print(" ")
print("3:ADD NEW COLLECTION")
print(" ")
print("4:SEARCH A SHOE")
print(" ")
print("5:MODIFY CUSTOMER DETAILS")
print(" ")
print("6:ADD DISCOUNTS")
while v in 'yY':
v_choice=int(input("enter the choice"))
if v_choice==1:
cust_details()
elif v_choice==2:
show_details()
elif v_choice==3:
new_collections()
elif v_choice==4:
search_shoe()
elif v_choice==5:
modify_details()
elif v_choice==6:
discount()
v=input("do u want to continue" )
