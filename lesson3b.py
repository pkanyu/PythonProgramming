# Tuples : ()
# Properties: ordered, duplicates allowed, immutable (unchangeable) 
# Data from database  to/from an application are enclosed on a tupple for security reasons


counties = ("Nairobi", "Baringo" , "Siaya")
print(type(counties))


# Create a tuple of one item .
# Print the type.


county= ("Nairobi",)
print(type(counties))


newCounty=tuple("Nakuru")
print(type(newCounty))

print(counties[0])

# Methods

print(counties.index("Siaya"))

newCounties = list (counties)

newCounties.append("Muranga")

counties = tuple(newCounties)
print(counties)