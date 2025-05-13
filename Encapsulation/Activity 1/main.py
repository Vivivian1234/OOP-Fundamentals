from bank_account import BankAccount

def main():
    account_number = int(input("Input account number: "))
    balance = int(input("Input balance number: "))
    owner_name = input("Input owner name: ")

    user_account = BankAccount(account_number, balance, owner_name)

    print(f'\nAccount Number: {user_account.get_account_number()}')
    print(f'Balance Number: ${user_account.get_balance()}')
    print(f'Owner name: {user_account.get_name()}\n')

    while True:
        try:
            action = int(input("What would you like to do? \n- 1. Withdraw \n- 2. Deposit \n- 3. Exit\n"))
        except ValueError:
            print("\nInvalid input. Please enter a number.\n")
            continue

        if action == 1:
            amount = int(input("How much would you like to withdraw? "))
            user_account.withdraw(amount)
        elif action == 2:
            amount = int(input("How much would you like to deposit? "))
            user_account.deposit(amount)
        elif action == 3:
            print("\nThank you for using the BankAccount program.\n")
            break
        else:
            print("Invalid option. Please try again.")

        print(f'\nAccount Number: {user_account.get_account_number()}')
        print(f'Balance Number: ${user_account.get_balance()}')
        print(f'Owner name: {user_account.get_name()}\n')

if __name__ == "__main__":
    main()
