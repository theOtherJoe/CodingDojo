class BankAccount:
    def __init__(self, account_name, int_rate, balance):
        self.bank_account_name = account_name
        self.int_rate = float(int_rate / 100)
        if balance == " ":
            self.balance = 0
        else:
            self.balance = balance
    
    def create_new_account(self, account_name, int_rate, balance):
        self.bank_account_name = account_name
        self.int_rate = float(int_rate / 100)
        if balance == " ":
            self.balance = 0
        else:
            self.balance = balance
        return self

    def deposit(self, account_name, amount):
        self.bank_account_name = account_name
        self.balance += amount
        return self

    def withdraw(self, account_name, amount):
        self.bank_account_name = account_name
        if self.balance < 0:
            print(f"Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        else:
            self.balance -= amount
        return self

    def display_account_info(self, account_name):
        self.bank_account_name = account_name
        return self.balance

    def yield_interest(self, account_name):
        self.bank_account_name = account_name
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self

class User:
    def __init__(self, name, email, account_name):
        self.name = name
        self.email = email
        self.account = BankAccount(account_name, int_rate=2, balance=0)

    def new_account(self, account_name, int_rate=2, balance=0):
        self.account.create_new_account(account_name, int_rate=2, balance=0)
        return self

    def make_deposit(self, account_name, amount):
        self.account.deposit(account_name, amount)
        return self

    def make_withdrawal(self, account_name, amount):
        self.account.withdraw(account_name, amount)
        return self

    def display_user_balance(self, account_name):
        return print(f"{self.name}'s Account Balance: ${self.account.display_account_info(account_name)}")

    def transfer_money(self, account_name, amount, name):
        name.make_deposit(account_name, amount) 
        self.make_withdrawal(account_name, amount)
        print(f"{self.name}'s account balance is now: ${self.account.display_account_info(account_name)}")
        print(f"{name.name}'s account balance is now: ${name.account.display_account_info(account_name)}")
        return self

ruth = User("Babe Ruth", "theBabe@nyyankees.com", "Babe account1")
lou = User("Lou Gehrig", "theIronHorse@nyyankees.com", "Lou account1")
joe = User("Joe Dimaggio", "theYankeeClipper@nyyankees.com", "Joe account1")

ruth.make_deposit("Babe account1", 500000).make_deposit("Babe account1", 24500).make_deposit("Babe account1", 1250000).make_withdrawal("Babe account1", 350000).display_user_balance("Babe account1")

lou.make_deposit("Lou account1", 5000000).make_deposit("Lou account1", 124500).make_withdrawal("Lou account1", 35000).make_withdrawal("Lou account1", 88000).display_user_balance("Lou account1")

joe.make_deposit("Joe account1", 3500000).make_withdrawal("Joe account1", 450000).make_withdrawal("Joe account1", 12000).make_withdrawal("Joe account1", 4200).display_user_balance("Joe account1")

ruth.transfer_money("Babe account1", 15000, joe)