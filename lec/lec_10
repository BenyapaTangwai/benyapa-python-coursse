class BankAccount:
    def __init__(self,accountNumber,name,balance):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance

    def Deposit(self,amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}.\nNew balance: ${self.balance}\n")
        else:
            print("Deposit amount must be positive\n")
        
    def Withdraw(self,amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}.\nNew balance: ${self.balance}\n")
        elif amount > self.balance:
            print("Insufficient funds\n")
        else:
            print("Withdrawal amount must be positive\n")
        
    def bankFees(self):
        fee = self.balance * (5/100)
        self.balance -= fee
        print(f"Bank fees are charged at a rate of 5%.\nNew balance: ${self.balance}")
    
    def display(self):
        print(f"Account Number: {self.accountNumber}")
        print(f"Name: {self.name}")
        print(f"Balance: {self.balance}\n")

account = BankAccount("123-456-7890","Ben",2000)
account.display()
account.Deposit(200)
account.Withdraw(300)
account.bankFees()