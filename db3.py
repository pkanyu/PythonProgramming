# DELETE
# connection

import pymysql
connection = pymysql.connect(host='localhost', user='root', password='',database='MpesaTestDB')
print("Connection Successful")


#cursor
cursor=connection.cursor()

#data
emp_id = 4
sql = "delete from employees where emp_id = %s"
cursor.execute(sql,emp_id)

connection.commit()
print("Record Deleted Successfully")

