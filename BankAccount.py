import random

#Defined BankAccount
#random.randint gets random integer
class BankAccount:
    def __init__(self, fullname):
        self.name = fullname
        self.account_number = random.randint(91467395)
        self.balance = 0

#Define methods for BankAccount