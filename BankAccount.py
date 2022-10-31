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
        self.balance += amount
        print(f'Amount deposited: {amount} new balance: {self.balance}')
        return self.balance
    
    def withdraw(self, amount):
        """
        Function substracts a specificed amount from the user's balance.
        Displays a message for the amount wiuthdrawn.
        """
        self.balance -= amount
        if self.balance < 0:    # For situations only the user knows without explicitly stating exactly. 
            print("Insufficent funds.")
            self.balance = self.balance - 10 #This is an overfraft fee
            return self.balance
        else:
            print(f'Amount withdrawn: {amount} new balance: {self.balance}')
            return self.balance

    def get_balance(self):
        """
        Displays user's current account balance.
        No parameters needed since it's already declared.
        """
        print(f'Your current balance is: {self.balance}')

    def add_interest(self, monthly_interest):
        """
        Adds uinterest to the user's balance.
        Annual interest rate 1% (0.083% monthly)
        """
        interest = self.balance * 0.00083
        self.balance += interest

    def print_statement(self):
        """
        Prints message to user with all information.
        Imbedded line break.
        """
        print(f'{self.full_name}\n {self.account_number}\n {self.balance}')


#Define 3 different user bank accounts. Refer back to Class BankAccount()

#Mitchell Hudson
mitchell_account = BankAccount("Mitchell Hudson")
mitchell_account.deposit(400000)
mitchell_account.print_statement()
mitchell_account.add_interest()
mitchell_account.print_statement()
mitchell_account.withdraw(150)
mitchell_account.print_statement

# Marty Marinda
marty_account = BankAccount("Marty Marinda")
marty_account.getbalance()
marty_account.deposit(1000)
marty_account.print_statement()
marty_account.add_interest()
marty_account.print_statement()