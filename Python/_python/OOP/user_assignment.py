class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    
    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawl(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print(self.account_balance)
        return self

    def transfer_money(self, amount, name):
        name.make_deposit(amount) 
        self.account_balance -= amount
        print(f"My account balance is now: {self.account_balance}")
        print(f"{name.name}'s account balance is now: {name.account_balance}")
        return self


ruth = User("Babe Ruth", "theBabe@nyyankees.com")
lou = User("Lou Gehrig", "theIronHorse@nyyankees.com")
joe = User("Joe Dimaggio", "theYankeeClipper@nyyankees.com")

ruth.make_deposit(500000).make_deposit(24500).make_deposit(1250000).make_withdrawl(350000).display_user_balance()

lou.make_deposit(5000000).make_deposit(124500).make_withdrawl(35000).make_withdrawl(88000).display_user_balance()

joe.make_deposit(3500000).make_withdrawl(450000).make_withdrawl(12000).make_withdrawl(4200).display_user_balance()

ruth.transfer_money(15000, joe)