# utils.py
from person import Person
from bank_account import BankAccount

def person_data():
    name = input("Enter the person's name:\n")
    person_obj = Person(name)
    
    while True:
        acc_num = int(input("Enter a 4-digit account number:\n"))
        init_balance = float(input("Enter the initial balance:\n"))
        
        account = BankAccount(acc_num, init_balance)
        person_obj.add_account(account)
        
        done = input("Are you done adding accounts? (yes/no):\n").strip().lower()
        if done == "yes":
            break
            
    return person_obj

def balance_summary(person_list):
    for person in person_list:
        total_balance = sum(account.balance for account in person.accounts)
        print(f"{person.name} : {total_balance:.2f}")