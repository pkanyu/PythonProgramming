# Import
#1. create a database connection to
#2. confirm the connection


# create 3 variable to hold, username, password, phone

#4. create a cursor to your connection

#5. write sql to save username, pasword and phone on users table
#6. Execute your sql
#7. commit your connection
#8. notify that record has been saved
import pymysql

connection = pymysql.connect(host='localhost', user='root',password='',database='MpesaTestDB')
print("Database connection successful")


# our data 
username = "chile"
password = "QObvH1234"
phone_number = +2547123456
user_id = None

cursor = connection.cursor()

sql = "insert into users (username, password, phone_number, user_id) values(%s,%s,%s,%s)"

#Execute the sql
data = (username,password,phone_number,user_id)
cursor.execute(sql,data)
# commit sql
connection.commit()
print("Record Saved Successfully")