# Python loops : Used to repeat a code a number of times based on a condition.
# message 100 times 

# print("Hello ")
# print("Hello")

# In python: for , while
# Kotlin: for, while , do-while
# In JS : for , while forEach()

# For Loop:
# syntax: for variable in sequence(collection)
#                  statements


# For Loop in range(): check the condition

for message in range(10):
    print(f"Hello {message} " )

# print the first 20 numbers
# for i 

print("======================================")
for i in range(20):
    print(i)


#range function with starting point.
print("========================")
for index in range(6,21):
    print(index
          )
    

# range function with increment/decrement
print("=======================")
condition =range(10,110,10)
for index in condition:
    print(index)

#Summarize:
#Default:range(starting 0,limit, increament 1)
#Modified: range(start, limit, interval/decrement(- interval))

print("=====================")
#print numbers form 100 t0 60, with interval of 10
for index in range(100,50,-10):
    print(index)