class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount

    def display(self):
        print("Account holder:", self.name)
        print("Balance:", self.balance)


name = input("Enter account holder name: ")
balance = float(input("Enter initial balance: "))

account = BankAccount(name, balance)

deposit_amount = float(input("Enter amount to deposit: "))
account.deposit(deposit_amount)

withdraw_amount = float(input("Enter amount to withdraw: "))
account.withdraw(withdraw_amount)

account.display()