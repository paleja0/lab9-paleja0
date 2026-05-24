import utils
from person import Person
from bank_account import BankAccount

def main():
    person_list = []

    while True:
        print("\nChoose an option:")
        print("1. Add a new person")
        print("2. Add an account to a person")
        print("3. Show all balances")
        print("4. Quit")
        
        option = input()

        if option == "1":
            new_person = utils.person_data()
            person_list.append(new_person)

        elif option == "2":
            name_to_find = input("Enter the person's name:\n")
            target_person = None
            
            for p in person_list:
                if p.name == name_to_find:
                    target_person = p
                    break
                    
            if target_person:
                acc_num = int(input("Enter a 4-digit account number:\n"))
                init_balance = float(input("Enter the initial balance:\n"))
                account = BankAccount(acc_num, init_balance)
                target_person.add_account(account)
            else:
                print("Person not found.")

        elif option == "3":
            if not person_list:
                print("No data to show.")
            else:
                utils.balance_summary(person_list)

        elif option == "4":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
