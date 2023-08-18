# Read all the data from the users table
# Import pymysql
import pymysql
connection = pymysql.connect(host='localhost', user='root', password='',database='MpesaTestDB')
print("Connection Successful")

# Make connection
cursor= connection.cursor()
# Sql
sql = "select * from users"

# Execute
cursor.execute(sql)

# Make count
count = cursor.rowcount

print(count)

# Check if the table is empty

if count == 0:
    print("No data")
else:
    # Bring my data
    data = cursor.fetchall()
    print(data)
