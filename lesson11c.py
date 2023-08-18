# Banking System
# Account

# Parent Class
class Bank:


    def usd_exchange_rate(self,currency,rate):
        rate *=currency
        print(f"Your new rate is {rate} ")

        

class Account(Bank):
    def __init__(self,name,pin,balance,accno,branch,status):
        if balance <=0:
            print("Account Balance cannot be Zero!")
        elif len(name) == 0:
            print("Please Enter Your Account Name! ")
        elif len(accno) !=6:
            print("Invalid Account Number")
        else:
            self.name = name
            self.pin = pin
            self.balance = balance
            self.accno = accno
            self.brance = branch
            self.status = status
    
    def withdraw(self):
        print("====WELCOME TO WITHDRAWALS===== \n")
        pin = int(input("Enter Your PIN:"))
        if pin == self.pin:
            print("===You Have Access=== \n")
            amount = int(input("Please Enter the Amount to Withdraw: "))
            if amount <= self.balance:
                print("Success!")
                print(f"You have Withdrawn Ksh. {amount} ")
                newBalance =self.balance - amount
                print(f"Your new Balance is {newBalance} ")
            else:
                print("Insufficient Account Balance!")
        else:
            print("Wrong PIN")
# check balance()
    def check_balance(self):
        print("===Balance ====")
        pin =int(input("Please Enter Your PIN: "))
        if pin == self.pin:
            print(f"Your Account Balance is Ksh.{self.balance} ")
        else:
            print("Wrong PIN")

    def menu(self):
        print("Please Enter an Option")
        print("1. Withdraw")
        print("2. Check Balance")

        
        option = int(input("Please Enter Your Choice: " ))
        if option ==1:
            self.withdraw()
        elif option ==2:
            self.check_balance()
    def win():
        sum=1+1
        return sum

account1 = Account(
    "Modcom Institue",
    1234,
    10000,
    "123456",
    "Westlands",
    "active"
)

#comment
#This is a commment
# account1.menu()

# account2 = Account(
#     input("Enter the Account Name: "),
#     int(input("Enter Your PIN: ")),
#     int(input("Enter the Amount You would like to Deposit: ")),
#     " ",
#     "Westlands Branch",
#     "active"
# )

# while True:
#     account2.menu()
account1.usd_exchange_rate(10000,0)
# account1.exchange(10000)
# In OOP Paradigm we follow some of its concepts:
#1. Inheritance : A child class can inherit states and behaviours of a parent class
#2. Abstraction : It hides complexities of the program by implementing interfaces
#3. Encapsulation : Classes can hide their information from other classes
#4. Polymorphism : An class can generate different instances 

# Method Overloading
# Method Overriding