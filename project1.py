# USSD : Accessible by short code e,g *444#
# Withdraw Function:
customer={
    "PIN": 2023,
    "name" : "Derrick Clerkson",
    "balance" : 15000,
    "status" : "inactive",
    "phone" : "+2547XXXXXX"
}

# Withdraw
def withdraw(pin,amount,agent_no):
   
    print("")
    if pin == customer["PIN"]:
        
        if amount <= customer["balance"]:
            print(f"Confirmed. Successfully withdrawn Ksh {amount} from Agent No. {agent_no} " )
            balance = customer["balance"] - amount
            print(f"Your Balance is {balance} ")
            print("Thank You!!")
        else:
            print("Insufficient Account Balance")
            print("Try Again!!!")
    else:
        print("====ACCESS DENIED====")
        print("")
        print("Wrong PIN")

# Deposit
def deposit(pin,amount):
    if customer["status"] == "active":
        if pin == customer["PIN"]:
          
            customer["balance"]+=amount
            print(f"Your Account Balance is now {customer['balance']} ")
    
             
        else:
            print("Wrong PIN")
            

    else:
        print("Please Activate Your Account \n Status: Not Active!!")


# check balance
def check_balance(pin):
    
        if customer["status"]=="active":
            if pin ==customer["PIN"]:
                print(f"Confirmed YOur Current Balance is {customer['pin']} ")
            else:
                print("Wrong Pin")
        else:
            print("Status Not Active")

# Change PIN
def change_pin(current,new,confirm):
    if customer["status"]=="active":
        if current == customer["PIN"]:
            if new == confirm:
                customer["PIN"]=new
            
                print(f"Change PIN Successful \n Your New PIN is {customer['PIN']} ")
            else:
                print("Failed,PIN Doesn't Match")
          
        else:
            print("Wrong pin!!")
    else:
        print("Status Not Active")

# Loans and Savings

def savings(pin,save_amount):
                if customer["status"] =="active":
                    if pin == customer["PIN"]:
                            customer["balance"]+=save_amount
                            print(f"You Current Balance is now {customer['balance']} ")
                    else:
                            print("Wrong PIN")
                else:
                    print("Please Activate Your account")

def loans(pin,loan_amount):
                    if customer["status"] =="active":
                        if pin == customer["PIN"]:
                                if loan_amount <=customer["balance"] * 80/100:
                                    print(f"Success! Your loan request has been approved. Your current loan amount is {loan_amount} ")
                                else:
                                    print("Loan request unsuccessful. The loan limit not reached")
                        else:
                            print("Wrong PIN")
                    else:
                        print("Please Activate Your account")


def choose():
        print("1. Savings")
        print("2. Loan Request")

def menu():
        print("SIMPLE MPESA USSD APP")
        print("======WELCOME========")
        print("\n")
        print("1.Withdraw")
        print("2.Deposit")
        print("3.Check Balance")
        print("4.Change PIN")
        print("5.Loans & Savings")
        print("6.Fuliza MPESA")
        print("0.Exit")
        print("")



        while True:
            option = int(input("Please Enter Your Choice: " ))
            if option == 1:
                withdraw(
                    int(input("Enter Your PIN: ")),
                    int(input("Enter the Amount: ")),
                    int(input("Enter the Agent Number: ")),

                )
            elif option == 2:
                deposit(
                    int(input("Enter Your PIN: ")),
                    int(input("Enter the Amount to Deposit: ")),
                )
            elif option ==3:
                check_balance(
                    int(input("Enter Your PIN: "))
                )
            elif option ==4:
                change_pin(
                    int(input("Enter Your Current PIN: ")),
                    int(input("Enter Your New PIN: ")),
                    int(input("Confirm Your PIN: "))
                )
            elif option ==5:
                choose()
                choice= int(input("Enter Option: "))
                
                if choice ==1:
                    savings(
                        int(input("Enter Your PIN: ")),
                        int(input("Please Enter the Amount You Want to Save: "))
                    )
                if choice ==2:
                    loans(
                        int(input("Enter Your PIN: ")),
                        int(input("Please Enter the Loan Amount: "))
                )
            elif option ==0:
                break
                
            else:
                print("Other Options on Development")
                

menu ()
