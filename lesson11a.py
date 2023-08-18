# OOP : style(paradigm) of programming where everything (real-world entities) is treated as an object. e,g car, person, road, object.
# Object : Real world entity that has states(properties) and behaviours(methods)
# States: Things that the object posses.
# Methods: Things that the object can do.
# Object: Instance of a class
# Instantiation: process of creating objects from a class.

# E,g Account: states(balance, name, pin, status) methods(withdraw,deposit...)
# Student: states(name, course, gender) methods(learn, exam, ...)

# Class: Blueprint(template) of an object because it will define properties and methods of an object

# class Shirt: properties(color, price, size), methods(purchase(), changeprice())


#shirt1(red, 300, XL) changeprice(250)
#shirt2(black, 1500, M) changeprice(1800)


# class: Design how squares look like
class Square:
    def __init__(self, width, height):
        self.width =width
        self.height =height

    def area(self):
        area_square = self.width * self.height
        print(f"The area is {area_square} ")


    def perimeter(self):
        perimeter_square = (self.width*4) 
        print(f"Perimeter is {perimeter_square} ")
        

# Objects : Treated as variables.
square1 = Square(5,5)
square1.area()
square1.perimeter()
square2 = Square(30, 30)
square2.perimeter()

name  = "bob"
print(type(name))
name.upper()
print(f"{name}")