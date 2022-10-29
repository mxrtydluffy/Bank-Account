import random

#Defined BankAccount
#random.randint gets random integer
class BankAccount:
    def __init__(self, fullname, acount_number, balance):
        self.name = fullname
        self.account_number = random.randint(91467395)
        self.balance = 0

#Define methods for BankAccount
    def deposit(self, amount):
        """
        Function adds inputed amount to account balance.
        Displays a message for a new updated balance.
        """
        self.balance = self.balance + amount
        return self.balance
    
    def withdraw(self, amount):
        """
        Function substracts a specificed amount from the user's balance.
        Displays a message for the amount wiuthdrawn.
        """
        self.balance = self.balance - amount
        if self.balance < 0:    # For situations only the user knows without explicitly stating exactly. 
            print('Error please try again')
        else:
            return self.balance

    def obtain_balance(self):
        """
        Displays user's current account balance.
        No parameters needed since it's already declared.
        """
        return self.balance

#Define 3 different user bank accounts. Refer back to Class BankAccount()