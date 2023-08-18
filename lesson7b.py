# For Loop in a Sequence(Collection)
# collection: string, list, tuples, dictionaries



#String Sequence
language= "Python"
for letter in language:
    print(letter)


print("========================")
#List Sequence
#loops with conditions
proLanguages =["Python","C", "Java", "JavaScript", "C#"]
for language in proLanguages:
    if language =="Java":
        print("Java Exists")


# Assumptions:
# 1.create a list of 8 counties in Kenya.
# 2.create two empty lists namely: single , double

# Task: 
# Iterate through the list of 8 counties checking whether it has either single name or double name.
# If it has single name append to single empty list, otherwise append to double empty list.

counties = ["Nairobi", "Taita Taveta", "Garisa", "Nakuru", "Uasin Gishu", "Homa Bay", "Murang'a", "Kakamega"]
double =[]
single =[]

for county in counties:
    if " " in county:
        double.append(county)
        
    else:
        single.append(county)

print(single)
print(double)

# others methods