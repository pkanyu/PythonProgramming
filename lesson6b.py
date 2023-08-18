# Triangle

side1 = int(input("Enter First Side in cm: "))
side2 = int(input("Enter the Second Side in cm: "))
side3 = int(input("Enter the Third side in cm: "))

# Equalateral
if side1 == side2 and side2 == side3:
    print("Equalateral")

# Isoscles
elif (side1 ==side2 and side2 != side3) or (side2==side3 and side3 != side1) or (side1 == side3 and side1 != side2):
    print("Isosceles")

elif (side1 != side2) and (side2 != side3) and (side3 != side1):
    print("Scalene")
