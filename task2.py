# cost = int(input("Enter the cost price: "))
# if cost > 100000:
#     print(f"The road tax is Rs {cost*15/100} ")
# elif cost > 50000 and  cost <= 100000:
#     print(f"The road tax is Rs {cost*10/100} ")
# elif cost <= 50000:
#     print(f"The road tax is Rs {cost*5/100} ")
# else:
#     print("Invalid cost price")



# day = int(input("Enter a number from one to seven: "))
# if day ==1:
#     print("Sunday")
# elif day ==2:
#     print("Monday")
# elif day ==3:
#     print("Tuesday")

# elif day ==4:
#     print("Wednesday")

# elif day ==5:
#     print("Thursday")

# elif day ==6:
#     print("Friday")

# elif day ==7:
#     print("Saturday")

# else:
#     print("Invalid number")


# per = int(input("Enter the percentage"))
# if per < 40:
#     print("Failes")
# elif per >=40 and per < 50:
#     print("Fair")
# elif per >=55 and per < 65:
#     print("Good")
# elif per >= 65:
#     print("Excellent")
# else:
#     print("Invalid Percentage!!")

# num = int(input("Enter a number that is a multiple of 5: "))
# if num%5 ==0:
#     print("Hello")
# else:
#     print("Bye")

# numb= int(input("Enter a number: "))
# if numb%7 ==0:
#     print("The number is divisible by 7")
# else:
#     print("The number is not divisible by 7")

year = int(input("Enter a year: "))
if year % 4 == 0 and year%100 !=0:
    print("This is a leap year")
elif year% 400 == 0:
    print("This is a leap year")
else:
    print("This is not a leap year")