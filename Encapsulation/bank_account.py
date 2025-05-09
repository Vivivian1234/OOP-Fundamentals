class BankAccount:
    def __init__(self, account_number, balance, owner_name):
        if account_number < 0:
            raise ValueError("Account number cannot be negative. Please try again.")
        
        self.__account_number = account_number
        self.__balance = balance
        self.__owner_name = owner_name

    def get_account_number(self):
        return self.__account_number

    def get_balance(self):
        return self.__balance

    def get_name(self):
        return self.__owner_name
    
    def withdraw(self, amount):
        if amount > self.__balance:
            print("Withdrawal incomplete; not enough funds.")
        else:
            self.__balance -= amount
            print(f'Withdrawal complete. New balance: ${self.__balance}')

    def deposit(self, amount):
        self.__balance += amount
        print(f'Deposit complete. New balance: ${self.__balance}')

account_number = int(input("Input account number: "))
balance = int(input("Input balance number: "))
owner_name = input("Input owner name: ")

user_account = BankAccount(account_number, balance, owner_name)

print(f'\nAccount Number: {user_account.get_account_number()}')
print(f'Balance Number: ${user_account.get_balance()}')
print(f'Owner name: {user_account.get_name()}')

action = int(input("What would you like to do? \n- 1. Withdraw \n- 2. Deposit \n- 3. Exit\n"))

while action != 3:
    if action == 1:
        withdraw_money = int(input("How much would would like like to withraw? "))
        user_account.withdraw(withdraw_money)
        action = int(input("What would you like to do? \n- 1. Withdraw \n- 2. Deposit \n- 3. Exit\n"))
    elif action == 2:
        deposit_money = int(input("How much would you like to deposit? "))
        user_account.deposit(deposit_money)
        action = int(input("What would you like to do? \n- 1. Withdraw \n- 2. Deposit \n- 3. Exit\n"))
    else:
        print("Input not accepted. Please try again.")
        action = int(input("What would you like to do? \n- 1. Withdraw \n- 2. Deposit \n- 3. Exit\n"))

print ("Thank you do using the BankAccount program.")