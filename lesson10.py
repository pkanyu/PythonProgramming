# Error Handling/Exception Handling ...
# Handling errors created by the users to avoid system from crashing
# we use try, except block
# try: houses a code that might generate an error from the user
# except/catch: where the error is handled before the system crashes


# while True:
#     try:
#         number = int(input("Enter a digit: "))
#         print(f"You have entered {number} ")
#     except:
#         print("Please Enter a Valid input: ")
try:
    num1 = int(input(" Enter first number: "))
    num2 = int(input(" Enter second number: "))

    division = num1/num2
    print(division)
except:
    print("Invalid ..Zero cannot be an input!")

# Handle the error above...
# Types of Exceptions in Python


# Object Oriented Programming...
# classes
# objects
