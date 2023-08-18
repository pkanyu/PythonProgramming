# Functions: A block of code that performs a specific task on the system, that only executes when it is called(referenced)
# Mpesa USSD Application, eg Send Money, Deposit, Withdraw, Check Balance,Change PIN.

# Types of functions
# Inbuilt Functions : Already existing on the project.e,g print(), input(), range()
# User-specific(Defined) : Created by a developer, then call when needed.e,g send_sms(), encripty(), mpesa()

# Defining a function :
# def function_name():
#       code block

def greet():
    print("Hello, Welcome to Functions")
# Calling a function
# function_name(): Exit the function and call it


greet()

def add():
    number1 = int(input("Enter first number: "))
    number2 = int(input("Enter second number: "))
    sum = number1 + number2
    print(sum)

# add()
# Create a function to perfom simple interest
# call the function

def simple_interest():
        # Simple Interest
    principle = 30000
    rate = 6
    time = 10

    interest = (principle * rate * time )/100
    print("The simple interest is :",interest)

    # Get the total amount
    totalAmount = principle + interest
    print("The total Amount is:",totalAmount)
simple_interest()