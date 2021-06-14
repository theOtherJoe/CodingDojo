class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    
    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdrawl(self, amount):
        self.account_balance -= amount

    def display_user_balance(self):
        print(self.account_balance)
        
    def transfer_money(self, amount, name):
        name.make_deposit(amount) 
        self.account_balance -= amount
        print(f"My account balance is now: {self.account_balance}")
        print(f"{name.name}'s account balance is now: {name.account_balance}")


ruth = User("Babe Ruth", "theBabe@nyyankees.com")
lou = User("Lou Gehrig", "theIronHorse@nyyankees.com")
joe = User("Joe Dimaggio", "theYankeeClipper@nyyankees.com")

ruth.make_deposit(500000)
ruth.make_deposit(24500)
ruth.make_deposit(1250000)
ruth.make_withdrawl(350000)
ruth.display_user_balance()

lou.make_deposit(5000000)
lou.make_deposit(124500)
lou.make_withdrawl(35000)
lou.make_withdrawl(88000)
lou.display_user_balance()

joe.make_deposit(3500000)
joe.make_withdrawl(450000)
joe.make_withdrawl(12000)
joe.make_withdrawl(4200)
joe.display_user_balance()

ruth.transfer_money(15000, joe)