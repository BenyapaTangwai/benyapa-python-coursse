class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        return f"Deposit {amount}"
    
    def withdraw(self, amount):
        if 0 < amount and amount <= self.balance:
            self.balance -= amount
            
    