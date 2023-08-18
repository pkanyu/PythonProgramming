# Data types
# We specify the format(type) of data stored on a variable. e,g number, letter, collection...
# Specify the operations done on that variable
# In python: 
# Integers (int): Numbers without decimals, e,g age, month...
# Floating Points (floats) : Numbers with decimal places e,g distance, height, speed...
# Strings (str) : Sequence of character enclosed inside either a double or a single quotes e,g name, course
# Booleans (bool) : A value having only two instances e,g True , False

# Collection (Arrays) : list, tuple , dictionary , set

#Strings
#type()
#Escape Sequence: used to introduce special character inside a strings \',\n
message = "I love programming"
print(type(message))

weather = ' It\'s a Chilly Morning'
print(weather)

paragraph = 'This is the first line,\nThis is the second line'
print(paragraph)

firstmessage = 'I love '
secondmessage = " Python"

#Concatenation - merge strings (+)

wholeMessage = firstmessage + secondmessage
print(wholeMessage)

#len() : Returns the number of characters in a string.
password = input("Enter your password:")
print(len(password))