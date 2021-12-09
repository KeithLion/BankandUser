class User:

    def __init__(self,name,balance):
        self.name = name
        self.account = BankAccount(int_rate=0.07,balance = balance)

    def make_deposit(self,amount):
        self.account.deposit(amount)

    def make_withdraw(self,amount):
        self.account.withdraw(amount)

    def display_user_balance(self):
        print(f'User:{self.name}, Balance:{self.account.account}')


class BankAccount:

    def __init__(self,int_rate,balance):
        self.intrest = int_rate
        self.account = balance
    
    def deposit(self,amount):
        self.account += amount
    
    def withdraw(self,amount):
        if (self.account - amount) > 0:
            self.account -= amount
        else:
            print('Insufficient funds: charging $5 fee')
            self.account - 5

    def display_account(self):
        print(f'Balance:{self.account}')
    
    def yield_intrest(self):
        if (self.account > 0):
            self.account += self.account*0.07

