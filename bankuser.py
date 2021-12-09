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
