import mysql.connector 
import random

mydb=mysql.connector.connect(host='localhost',user='root',password='3109') 
mycursor=mydb.cursor()

sql="Create Database IF NOT EXISTS MOVIE"
mycursor.execute(sql)


mycursor=mydb.cursor() 
mycursor.execute("Use MOVIE")

query4 = "CREATE TABLE IF NOT EXISTS silver(Customer_ID varchar(50), movie_name varchar(50), Amount int)" 
mycursor.execute(query4)


query5 = "CREATE TABLE IF NOT EXISTS theatre (Name varchar(50), Phone bigint, No_Tickets integer, Sex varchar(10), First_Name varchar(50), Last_Name varchar(50), Email_ID varchar(100), Mode_payment varchar(50))"
mycursor.execute(query5)


query6 = "CREATE TABLE IF NOT EXISTS imax (Customer_ID varchar(50), movie_name varchar(50), Amount int)" 
mycursor.execute(query6)

query7 = "CREATE TABLE IF NOT EXISTS 4dx (Customer_ID varchar(50), movie_name varchar(50), Amount int)"
 
mycursor.execute(query7) 
if mydb.is_connected():
    print(" THUNDER THEATRE BOOKING")
    print("\n\nTHUNDER THEATRE")
    ch = input("Do you want to check the show details (yes/no): " )

if ch=='no' or ch == 'NO':
    print("thanks for your visit")

    

if ch == 'yes' or ch == 'YES': print("*" * 80)
print("	SHOW DETAILS	")
print("*" * 80)
print("Select Shows (a.Morning Show /b.Noon Show/c. Night Show")
sh = input("Enter your choice: ") 
if sh == 'a':
    print("Time: 9:00 A.M")
    print("*" * 30, " Movies", "*" * 30) 
    print("Screen 1. Asuran")
    print("Screen 2. Pollathavan")

if sh == 'b':
    print("Time: 1:00 P.M")
    print("*" * 30, " Movies", "*" * 30) 
    print("Screen 1. Aadukalam")
    print("Screen 2. Vadachennai")

if sh == 'c':
    print("Time: 10:00 P.M")
    print("*" * 30, " Movies", "*" * 30) 
    print("Screen 1. Thiruchitrambalam")
    print("Screen 2.  Raayan")

print("CUSTOMER DETAILSGATEWAY") 
v_mname = input("Enter the movie name: ")
v_phone = input("Enter your Phone number: ")
v_tic = input("Enter total tickets: ")
v_sex = input("Enter your sex: ")
v_fname = input("Enter your first name: ") 
v_lname = input("Enter your last name: ") 
v_Email_ID = input("Enter your Email ID: ")
v_mpayment = input("Enter mode of payment (Debit or Credit card/UPI/Net Banking): ")
print("Type OK to Generate your one time Customer ID") 
m = input("Enter OK: ")
if m == 'OK' or m == 'ok': choices = list(range(1000)) 
random.shuffle(choices)
print("Your Member_ID is", choices.pop())
v_ins = "INSERT INTO theatre VALUES ('{}', {}, '{}', '{}', '{}', '{}', '{}','{}')".format(v_mname, v_phone, v_tic, v_sex, v_fname, v_lname, v_Email_ID, v_mpayment)
mycursor.execute(v_ins) 
mydb.commit()

print("	SCREEN AND SEAT BOOKING GATEWAY		")
print("1. GOLD [4dx] Ticket Booking") 
print("	Price per Ticket: Rs.1500 ") 
print("2. IMAX Ticket Booking")
 
print("	Price per Ticket: Rs.850 ") 
print("3. Silver Ticket Booking") 
print("	Price per Ticket:  Rs.500  ") 
    
ch = int(input("Enter your choice: "))
if ch == 1:
    print("WELCOME TO GOLD 4DX CINEMA BOOKING") 
a = input("Enter your one time Customer ID: ")
c = input("Enter your movie name: ")
d = int(input("Enter the number of tickets: ")) 
total = d * 1500
print("Bill for the tickets:", total) 
pswd = input("Your payment OTP: ")
sks = input("Your complimentary snacks (chips/popcorn/no): ") 
dd = input("Your complementary drink (coke/pepsi/no): ")
v_dx = "INSERT INTO 4dx VALUES ('{}', '{}', {})".format(a, c, total) 
mycursor.execute(v_dx)
mydb.commit() 
print("TICKETBOOKED")
print("/ENJOY THE MOVIE AND HAVEFUN")


if ch == 2: print("WELCOMETO IMAX TICKET BOOKING") 

aa = input("Enter your one time Customer ID: ")
cc = input("Enter your movie name: ")
dd = int(input("Enter number of tickets: ")) 
ttotal = dd * 850
print("Bill for the tickets:", ttotal) 
pswd = input("Your payment OTP: ")
sks = input("Your complimentary snacks (chips/popcorn/no): ") 
dd = input("Your complementary drink (coke/pepsi/no): ")
v_dy = "INSERT INTO imax VALUES ('{}', '{}', {})".format(aa, cc, ttotal)
mycursor.execute(v_dy) 
mydb.commit() 
print(" TICKET BOOKED ")
print("ENJOY THE MOVIE AND HAVE FUN")
breakpoint;

if ch == 3: 
    print("WELCOME TO SILVER TICKET T0 BOOKING") 
    aaa = input("Enter your one time Customer ID: ")
    ccc = input ("Enter your movie name :")
    ddd = int(input("Enter number of Tickets: ")) 
    tttotal=ddd*500
    print("Bill for the tickets:",tttotal) 
    pswd= input("Your payment OTP :")
    v_dz="insert into silver values( '{}','{}',{})".format(aaa,ccc,tttotal) 
    mycursor.execute(v_dz)
    mydb.commit()
 
    print ("TICKET BOOKED")
    print ("ENJOY THE MOVIE AND HAVEFUN") 

    
else:
    print("Thanks for visiting")
