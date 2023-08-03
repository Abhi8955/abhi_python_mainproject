import re
import sys

class Bank:
    balance = 0
    name = ""
    ac_num = ""
    ac_type = ""

    def Ac_open(self):
        self.name = input("Enter your name: ")
        self.ac_type = input("Enter account type: ")
        self.ac_num = input("Enter your account number: ")
        if len(self.ac_num) != 10:
            print("Invalid account number length. Program terminated.")
            sys.exit(1)

    def Deposit(self):
        amount = int(input("Enter Deposit Amount: "))
        if amount > 1000:
            self.balance += amount
            print("Deposit successful.")
        else:
            print("Deposit failed. The required balance is not met.")

    def Withdraw(self):
        amount = int(input("Enter Withdraw Amount: "))
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawal successful.")
        else:
            print("Withdrawal unsuccessful. Insufficient balance.")

    def Statement(self):
        print("Account Name:", self.name)
        print("Account Number:", self.ac_num)
        print("Account Type:", self.ac_type)
        print("Current Balance:", self.balance)


x = Bank()
x.Ac_open()
x.Deposit()
x.Withdraw()
x.Statement()
