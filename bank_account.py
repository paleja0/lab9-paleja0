# bank_account.py
class BankAccount:
    def __init__(self, account_number, balance=0.0):
        self.account_number = int(account_number)
        self.balance = float(balance)

    def deposit(self, amount):
        self.balance += float(amount)

    def withdraw(self, amount):
        if float(amount) > self.balance:
            return -1
        else:
            self.balance -= float(amount)
            return 0

    def __str__(self):
        num_str = str(self.account_number)
        last_two = num_str[-2:]
        return f"Account Number: **{last_two}\nCurrent Balance: {self.balance:.2f}"