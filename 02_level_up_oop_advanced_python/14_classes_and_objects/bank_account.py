class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self.balance += amount
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
    def get_balance(self):
        return self.balance
    def display(self):
        print(f"{self.owner}: Rs {self.balance:,.2f}")

account_a = BankAccount("Prathmesh", 20000)
account_b = BankAccount("Pranav", 5000)

print("Before Transfer:")
account_a.display()
account_b.display()

transfer_amount = 3000
print(f"Transferring Rs {transfer_amount:,.0f} "
      f"from {account_a.owner} to {account_b.owner}...\n")
try:
    account_a.withdraw(transfer_amount)
    account_b.deposit(transfer_amount)
except ValueError as e:
    print(f"Error: {e}")

print("After Transfer:")
account_a.display()
account_b.display()

print("Testing edge cases:")

try:
    account_a.deposit(-500)
except ValueError as e:
    print(f"Error: {e}")

try:
    account_a.withdraw(10000)
except ValueError as e:
    print(f"Error: {e}")

try:
    account_a.withdraw(0)
except ValueError as e:
    print(f"Error: {e}")

print(f"Prathmesh current balance: Rs {account_a.get_balance():,.2f}")