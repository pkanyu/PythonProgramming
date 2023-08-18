#Call functions from lesson9a library/module
#Keywords: 

#1.import: Used to call all the functions from a library
#syntax: import lesson9a

# import lesson9a

# #call the functions
# #syntax: filename.function()

# lesson9a.add(3,6)
# lesson9a.multiply(4,5)

# 2. from: calling specific functions from a module
# syntax: from filename import function

from lesson9a import *
subtract(10,6)
add(3,5)
divide(10,2)

# Types of modules: 
# 1. user-defined modules : created by a developer
# 2. Inbuilt Modules: Already existing modules

import math

ans= math.sqrt(64)
print(ans)

numbers=[3,5,6,7]
import random
result =random.shuffle(numbers)
print(result)


#research on inbuilt modules in python

#3. Modules from internet

import flask
import pygame

#syntax: pip3 isntall module 
#Research on popular python modules for:
#1. Web Applications
# 2.Machine Learning/Artificial Intelligence/Deep Learning
# 3.Data Analysis
# 4.Cyber Security
# 5.Gaming
# 6.Graphics
# 7.Sounds(Speech Recognition)