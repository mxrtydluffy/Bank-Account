import random

#Defined BankAccount
#random.randint gets random integer
class BankAccount:
    def __init__(self, full_name, account_number, balance = 0):
        self.full_name = full_name
        self.account_number = account_number
        self.balance = balance

#Define methods for BankAccount
    def deposit(self, amount):
        """
        Function adds inputed amount to account balance.
        Displays a message for a new updated balance.
        """
        self.balance += amount
        print(f'Amount Deposited: ${amount} New Balance: ${self.balance}')
        return self.balance
    
    def withdraw(self, amount):
        """
        Function substracts a specificed amount from the user's balance.
        Displays a message for the amount wiuthdrawn.
        """
        self.balance -= amount
        if self.balance < 0:    # For situations only the user knows without explicitly stating exactly. 
            print("Insufficent funds.")
            self.balance = self.balance - 10 #This is an overdraft fee
            return self.balance
        else:
            print(f'Amount Withdrawn: ${amount} New Balance: ${self.balance}')
            return self.balance

    def get_balance(self):
        """
        Displays user's current account balance.
        No parameters needed since it's already declared.
        """
        print(f'Your current balance is: ${self.balance}')

    def add_interest(self):
        """
        Adds uinterest to the user's balance.
        Annual interest rate 1% (0.083% monthly)
        """
        interest = self.balance * 0.00083
        self.balance += interest
        return self.balance

    def print_statement(self):
        """
        Prints message to user with all information.
        Imbedded line break.
        """
        print(f'{self.full_name}\n {self.account_number}\n {self.balance}')

#--------------------------------------------------------------------------------------------

#Define 3 different user bank accounts. Refer back to Class BankAccount()

#Mitchell Hudson
mitchell_account = BankAccount("Mitchell Hudson", "37509834")
mitchell_account.deposit(400000)
mitchell_account.print_statement()
mitchell_account.add_interest()
mitchell_account.print_statement()
mitchell_account.withdraw(150)
mitchell_account.print_statement

# Marty Marinda
marty_account = BankAccount("Marty Marinda", "49710467")
marty_account.print_statement()
marty_account.deposit(1000)
marty_account.print_statement()
marty_account.add_interest()
marty_account.print_statement()

#Robert Johnson
robert_johnson = BankAccount("Robert Johnson", "34501938")
robert_johnson.deposit(35000)
robert_johnson.print_statement()
robert_johnson.add_interest()
robert_johnson.print_statement()
robert_johnson.withdraw(5700)
robert_johnson.print_statement()