# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 01:46:33 2024

@author: Namita
"""

class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number  # Public attribute
        self.__balance = balance              # Private attribute (encapsulated)

    def __apply_fees(self):                   # Private method
        # Assume a 1% fee is applied on each operation (just an example)
        fee = self.__balance * 0.01
        self.__balance -= fee
        print(f"A fee of {fee} was applied. New balance: {self.__balance}")

    def deposit(self, amount):
        if amount > 0:
            print(f"Deposited {amount}$")
            self.__balance += amount
            self.__apply_fees()   # Call the private method after Deposit
        else:
            print("Deposit amount must be positive!")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            print(f"Withdrew {amount}$")
            self.__balance -= amount
            self.__apply_fees()               # Call the private method after withdrawal
        else:
            print("Insufficient balance or invalid amount!")

    def get_balance(self):
        return self.__balance                 # Getter to check the balance

#Main Program 
print("Account Statement")
account = BankAccount("Account No : ABNA 0020 1234", 500)
print(account.account_number)                # Public attribute is accessible
try:
    print(account.__balance)                     # private attribute is Not accessible
    
except AttributeError:
    print("Sorry, You Are Trying to print balance, it is encapsulated")


account.deposit(200)                         # Depositing money (fee applied)
account.withdraw(100)                        # Withdrawing money (fee applied)

print(f"Your current Balance is {account.get_balance()}")                 # Accessing private balance via getter

# Trying to access the private/encapsulated method directly will fail
try:
    account.__apply_fees()  # This will raise an AttributeError as this method is private  
except AttributeError:
    print("Sorry, You Can not dirtectly apply fees it is encapsulated")

