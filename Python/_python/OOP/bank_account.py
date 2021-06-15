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
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self

account1 = BankAccount(1, 50)
account2 = BankAccount(1, 100)

account1.deposit(50).deposit(100).deposit(5000).withdraw(125).yield_interest().display_account_info()
account2.deposit(10000).deposit(126).withdraw(45).withdraw(200).withdraw(1200).withdraw(275).yield_interest().display_account_info()