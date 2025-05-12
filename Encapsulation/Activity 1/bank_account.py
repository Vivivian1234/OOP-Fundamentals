
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
            print("\nWithdrawal incomplete; not enough funds.")
        else:
            self.__balance -= amount
            print(f'\nWithdrawal complete. New balance: ${self.__balance}')

    def deposit(self, amount):
        self.__balance += amount
        print(f'Deposit complete. New balance: ${self.__balance}')