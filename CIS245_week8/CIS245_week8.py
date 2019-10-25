"""
Name: CIS245_week8.py
Programmer: Jacob Hayes
Date: 20 Oct 2019
Purpose: Create a CheckingAccount and SavingsAccount object from a parent BankAccount class with added user interactability
"""

#relevant import statements here
from decimal import Decimal
import sys #to exit the program
import locale #for currency
locale.setlocale(locale.LC_ALL,'')


#------------------------------------------------------------------------#
#################################FUNCTIONS################################
#------------------------------------------------------------------------#

def Show_Menu():
    return input("\n(1) Checking\n(2) Savings\n(3) Exit Program\n\n")

def Show_Checking_Menu():
    #check if the user has a checking account
    if(hasCheckingAccount == 1):
        while 1:
            user_input = input("\nChecking Menu\n(1) Withdrawal\n(2) Deposit\n(3) Get Balance\n(4) Back\n\n")

            if(user_input == "1"):
                while 1:
                    try:
                        amt = float(input("How much would you like to withdraw? "))
                        checking.withdrawal(amt)
                        break
                    except ValueError:
                        continue
            elif(user_input == "2"):
                while 1:
                    try:
                        amt = float(input("How much would you like to deposit? "))
                        checking.deposit(amt)
                        break
                    except ValueError:
                        continue
            elif(user_input == "3"):
                checking.getBalance()
            else:
                #return to the calling function
                return
    else:
        print("You haven't opened a checking account with us!")

def Show_Savings_Menu():
    #check if the user has a savings account
    if(hasSavingsAccount == 1):
        while 1:
            user_input = input("\nSavings Menu\n(1) Withdrawal\n(2) Deposit\n(3) Get Balance\n(4) Back\n\n")

            if(user_input == "1"):
                while 1:
                    try:
                        amt = float(input("How much would you like to withdraw? "))
                        savings.withdrawal(amt)
                        break
                    except ValueError:
                        continue
            elif(user_input == "2"):
                while 1:
                    try:
                        amt = float(input("How much would you like to deposit? "))
                        savings.deposit(amt)
                        break
                    except ValueError:
                        continue
            elif(user_input == "3"):
                savings.getBalance()
            else:
                #return to the calling function
                return
    else:
        print("You haven't opened a savings account with us!")


#------------------------------------------------------------------------#
##################################CLASSES#################################
#------------------------------------------------------------------------#
class InsufficientBalanceError(Exception):
    pass

class BankAccount:
    #attributes
    accountNumber = 0
    balance = 0

    #no constructor for this parent class

    #methods
    def withdrawal(self, amt):
        try:
            if (amt <= self.balance):
                self.balance -= amt
                print("Your new balance is " + locale.currency(self.balance, grouping=True))
            else:
                raise InsufficientBalanceError()
        except InsufficientBalanceError:
            print("Your balance is not high enough to withdraw that amount!")
    def deposit(self, amt):
        self.balance += amt
        print("Your new balance is " + locale.currency(self.balance, grouping=True))
    def getBalance(self):
        print("Your balance is " + locale.currency(self.balance, grouping=True))

class CheckingAccount(BankAccount):
    #attributes
    fees = 5
    minimumBalance = 50

    #constructor
    def __init__(self, balance):
        self.balance = float(balance)

    #methods
    def deductFees(self):
        pass
    def checkMinimumBalance(self):
        if (self.balance < self.minimumBalance):
            print("Balance " + locale.currency(self.balance) + " too low to create account. Minimum balance " + locale.currency(self.minimumBalance))
            raise InsufficientBalanceError()

class SavingsAccount(BankAccount):
    #attributes
    interestRate = 0.02
    
    #constructor
    def __init__(self, balance):
        self.balance = balance

    #methods
    def addInterest(self):
        pass



#------------------------------------------------------------------------#
###################################MAIN###################################
#------------------------------------------------------------------------#

balance = 0
hasCheckingAccount = 0
hasSavingsAccount = 0

#loop the program forever until the user quits
while 1:
    #do they want to set up a checking account?
    user_input = input("Would you like to set up a checking account? Y/N ")
    if (user_input.upper() == "Y"): #if not, go to ANCHOR B
        #ask for amount to deposit, verify it is of a valid type
        #ANCHOR A
        while 1:
            try:
                input_balance = float(input("Balance to deposit in checking account: "))
                #create a checking account with the given amount. any errors are caught in following blocks.
                checking = CheckingAccount(input_balance)
                checking.checkMinimumBalance()
                hasCheckingAccount = 1
                break #GOTO ANCHOR B
            except ValueError:
                continue #GOTO ANCHOR A
            except InsufficientBalanceError:
                user_input = input("Try again? Y/N ")
                if (user_input.upper() == "Y"):
                    continue #GOTO ANCHOR A
                else:
                    break #GOTO ANCHOR B
    #ANCHOR B
    user_input = input("Would you like to set up a savings account? Y/N ")
    if (user_input.upper() == "Y"): #if not, go to ANCHOR C
        while 1:
            try:
                input_balance = float(input("Balance to deposit in savings account: " ))
                hasSavingsAccount = 1
                break
            except ValueError:
                continue
        savings = SavingsAccount(input_balance)
    #ANCHOR C
    while 1:
        user_input = Show_Menu()
        if (user_input == "1"):
            Show_Checking_Menu()
        elif(user_input == "2"):
            Show_Savings_Menu()
        else:
            sys.exit(0) #QUIT APPLICATION