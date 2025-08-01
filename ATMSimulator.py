from Account import Account
from datetime import date

def heading():
    today = date.today()
    name = "Synai Mclean"
    purpose = "Simulate an ATM"
    

    print(f"""
*************************************************
          Name: {name}\n\
          Purpose:{purpose}\n\
          Date: {today}
*************************************************
          """)

account = Account()

def id():
    
    id = int(input("Enter an id: "))
             
    while id > 9 or id < 0:

        id = int(input("Please enter a correct id 0 - 9: "))

    account.setId(id)

def mainMenu():
    
    while True:
        print("""
Main menu
1: check balance
2: withdraw
3: deposit
4: exit
""")
        choice = int(input("Enter a choice: "))
        

        if choice == 1:
            balance = account.getBalance()
            print(f"The balance is {balance}")
        elif(choice == 2):
            amount = float(input("Enter an amount to withdraw: "))
            account.withdraw(amount)
        elif(choice == 3):
            amount = float(input("Enter an amount to deposit: "))
            account.deposit(amount)
        elif(choice == 4):
            break
        
                  
       
        

def main():
    heading()
    while True:
        id()
        mainMenu()
   
    


    


    

    
                        
             
main()
