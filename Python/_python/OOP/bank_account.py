class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = float(int_rate / 100)
        if balance == " ":
            self.balance = 0
        else:
            self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance < 0:
            print(f"Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        else:
            self.balance -= amount
        return self

    def display_account_info(self):
        return self.balance

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=2, balance=0)
    
    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        return self.account.display_account_info()

    def transfer_money(self, amount, name):
        name.make_deposit(amount) 
        self.make_withdrawal(amount)
        print(f"My account balance is now: ${self.display_user_balance()}")
        print(f"{name.name}'s account balance is now: ${name.display_user_balance()}")
        return self

ruth = User("Babe Ruth", "theBabe@nyyankees.com")
lou = User("Lou Gehrig", "theIronHorse@nyyankees.com")
joe = User("Joe Dimaggio", "theYankeeClipper@nyyankees.com")

ruth.make_deposit(500000).make_deposit(24500).make_deposit(1250000).make_withdrawal(350000).display_user_balance()

lou.make_deposit(5000000).make_deposit(124500).make_withdrawal(35000).make_withdrawal(88000).display_user_balance()

joe.make_deposit(3500000).make_withdrawal(450000).make_withdrawal(12000).make_withdrawal(4200).display_user_balance()

ruth.transfer_money(15000, joe)