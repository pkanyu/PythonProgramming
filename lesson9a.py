# Modules/ Libraries
# A module is a python file containing python functions that can be called on another python file.

# Inside file: lesson9a we will create some functions
# Inside file: lesson9b we will call the functions from lesson 9a file
# Therefore lesson lesson9a is a module.
# create 3 functions.

def add(num1, num2):
    sum = num1 + num2
    print(f"Answer is {sum} ")



def multiply(num1, num2):
    product = num1 * num2
    print(f"Anser is {product} ")

#create subtract(), and divide()

def subtract(num1, num2):
    subtract=num1-num2
    print(f"Answer is {subtract} ")

def divide(num1, num2):
    division=num1/num2
    print(f"Answer is {division} ")