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

"""Bank Account
Methods with validation, object interaction, and error handling
Create a BankAccount class with owner (string) and balance (number, default 0) attributes.

Add the following methods:
- deposit(amount) — adds to balance. Raise ValueError if amount is zero or negative.
- withdraw(amount) — subtracts from balance. Raise ValueError if amount is zero or negative. Raise ValueError if amount exceeds current balance (no overdraft allowed).
- get_balance() — returns the current balance
- display() — prints owner name and current balance formatted as currency

Then create two accounts and implement a transfer between them:
- Withdraw from Account A
- Deposit into Account B
- Print both accounts before and after the transfer to verify

Test all edge cases:
- Depositing a negative amount
- Withdrawing more than the balance
- Withdrawing zero

Each edge case should print the error message, not crash the program.

Example output:

Before Transfer:
Amit: Rs 10,000.00
Priya: Rs 5,000.00

Transferring Rs 3,000 from Amit to Priya...

After Transfer:
Amit: Rs 7,000.00
Priya: Rs 8,000.00

Testing edge cases:
Error: Amount must be positive
Error: Insufficient funds
"""