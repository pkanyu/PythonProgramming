#  Functions with parameters/Arguments
 

def subtract():
    num1 = 50
    num2 = 20
    difference = num1 - num2
    print(difference)
# subtract()   
# subtract()   
# subtract()   

# Parameters: Variables that are passed when creating a function
# Arguments : Values passed while calling a function

def multiply(num1, num2):
    product = num1*num2
    print(product)

# multiply(5,6)
# multiply(7,8)
multiply(int(input("Enter First Value: ")),int(input("Enter Second Value: ")))

def greet(name):
    print(f"Hello {name} !")
greet("Anthony")