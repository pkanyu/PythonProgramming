# Electricity Bill Calculator

units = int(input("Enter the number of units: "))

if units <=100 and units >=0:
    print("There is no charge!")

elif units>100 and units <= 200:
    print(f"The charge is Rs{ (units-100)*5} ")


elif units >200:
    print(f"The charge is Rs{((100)*5)+(units-200)*10} ")

else:
    print("Invalid Units")