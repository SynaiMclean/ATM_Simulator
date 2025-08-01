from datetime import datetime

class Account:
    def __init__(self, id = 0, balance = 100.00 , annualInterestRate = 0.00):
        self.__id = id
        self.__balance = balance
        self.__annualInterestRate = annualInterestRate
        self.__dateCreated = datetime.now()

    #Accesors    
    def getId(self):
        return self.__id

    def getBalance(self):
        return self.__balance
    
    def getAnnualInterestRate(self):
        return self.__annualInterestRate

    def getDate(self):
        return self.__dateCreated
    
    
    #Mutator

    def setId(self, id):
        self.__id = id

    def setBalance(self, balance):
        self.__balance = balance
        
    def setAnnualInterestRate(self, annualInterestRate):
        self.__annualInterestRate = annualInterestRate;
        

    def getMonthlyInterestRate(self, annualInterestRate):
        return self.__annualInterestRate / 12

    def getMonthlyInterest(self, annualInterestRate):
        return self.__balance * getMonthlyInterestRate() / 100    
 
    def withdraw(self, amount):
         self.__balance -= amount
         
    def deposit(self, amount):
        self.__balance += amount
        

         
    



        
