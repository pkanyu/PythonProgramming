# SIMPLE LOGIN SYSTEM


user = {
    "username" : "user123",

    "password" : "1234",

    "timeline1" : {
        "username" : "Bigbuzz",
        "Posted" :"LIVE IN NAIVASHA"
    },

    "timeline2" : {
        "username": "Coderz",
        "posted" : "Working on my Bootstrap Project"
    }
}

# user authentication
username = input("Enter your username: ")
password = input("Enter your Password: ")
if username == user["username"] or password == user["password"]:
    print("======WELCOME TO FACEBOOK========")
    print(user["timeline1"])
    print("=================================")
    print(user["timeline2"])
else:
    print("==========ACCESS DENIED===========")
    print("===========TRY AGAIN==============")


# Task 1 :
# Attack(Hack) the system to grant access with only your username

# Task 2 :
# Grant Access with both wrong credentials


# Mpesa Appication
# Deposit
# Withdraw
# Check Balance
# Change Pin
# Send Money
username = input("Enter your username: ")
password = input("Enter your Password: ")
if not(username != user["username"] or password == user["password"]):
    print("======WELCOME TO FACEBOOK========")
    print(user["timeline1"])
    print("=================================")
    print(user["timeline2"])
else:
    print("==========ACCESS DENIED===========")
    print("===========TRY AGAIN==============")
