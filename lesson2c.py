 #BOOLEANS (bool)

isApproved = False
print(type(isApproved))


isAbsent = True


# Booleans with Comparison Operators
# We have the following: >, < , ==, >=, <=,!=
#Comparison Operators : used to compare one variable and another.


print(10 > 6)

# passwordSaved = "12345678"
# passwordRequested = input("Enter your password:")
# print(passwordSaved == passwordRequested) 
#Logical Operators : Compare the relationship between one condition and another condition.
#and  : returns True when BOTH conditons are True
#or :AT LEAST ONE condition is True
#not : NEGATES(opposite) a condition
username = 'admin'
password = '12345678'

usernameRequested = input("Enter Username: ")
passwordRequested = input("Enter Your Password: ")

print(not(username == usernameRequested or    password == passwordRequested))
