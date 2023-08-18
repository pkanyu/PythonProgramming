# READ OPERATION(SELECT ): Retrieving data from the Database

# Step 1. Database connection

import pymysql

connection = pymysql.connect(host='localhost', user='root',password='',database='MpesaTestDB')
print("Database connection successful")

# Step2. Create a connection cursor 
cursor = connection.cursor()

# Step3. Sql to read data

sql ="select * from employees"

# Execute
cursor.execute(sql)

# Step4. Check whether it is empty(rowcount)
count = cursor.rowcount
print(count)

if count == 0:
    print("No records found")
else:
    data = cursor.fetchall()
    print(data)