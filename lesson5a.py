# Control Flow : A way control program execution
# Three Categories:
# 1. Sequential control flow ; Default codes are executed line by line (no indentation)
# 2. Conditional control flow : Codes are executed based on some conditons
# 3. Iterative control flow : Codes are executed a number of times based on some condtions



# CONDITIONAL:
# We have 3 conditions, if , else, else if (elif), nested if 

#IF: 
# condition/expression: checked return booleans (True, False)
# Statements : Code that is executed when the condition is either True or False



age = 15
if age > 18:
    print(" ISSUED WITH ID")
else:
    print("PLEASE TRY NEXT TIME!")

# IF ELSE: One condition is checked  if the condition return True if statement is executed, otherwise the else statement is executed.


# Request the number from the user
# Applying the idea of modulus(%) and conditions
# Write a program to test whether a number is even(divisible by 2) or odd

number = int(input(" Enter the number: "))
if number%2 == 0:
    print("The number is even")
else:
    print("The number is odd")

