
from datetime import date
from collections import defaultdict
from math import isfinite
import shlex

from models import Transaction
from storage import load_transactions, save_transactions
#Transaction Operations
def add_transaction(transactions, parts):
    try:
        if len(parts) < 5:
            raise ValueError('Usage: add income|expense amount category "description" [YYYY-MM-DD]')
        transaction_type = parts[1].lower()
        amount = float(parts[2])
        category = parts[3]
        if not isfinite(amount) or amount <= 0:
            raise ValueError("Amount must be a positive valid number.")
        if len(parts) >= 6:
            transaction_date = date.fromisoformat(parts[-1])
            description = " ".join(parts[4:-1])
        else:
            transaction_date = date.today()
            description = " ".join(parts[4:])
        transaction = Transaction(
            type=transaction_type,
            category=category,
            amount=amount,
            date=transaction_date.isoformat(),
            description=description
        )
        transactions.append(transaction)
        if save_transactions(transactions):
            print(
                f"Added {transaction.type}: "
                f"Rs {transaction.amount:,.2f} "
                f"({transaction.category})"
            )
        else:
            transactions.remove(transaction)
            print("Transaction was not added because saving failed.")
    except (ValueError, TypeError) as error:
        print(f"Invalid transaction: {error}")
#List Transactions
def list_transactions(transactions):
    if not transactions:
        print("\nNo transactions found.")
        return
    print("\n========== TRANSACTIONS ==========")
    for transaction in transactions:
        symbol = "+" if transaction.type == "income" else "-"
        print(
            f"#{transaction.id} | "
            f"{transaction.date} | "
            f"{transaction.type.upper():7} | "
            f"{symbol} Rs {transaction.amount:,.2f} | "
            f"{transaction.category} | "
            f"{transaction.description}"
        )
    print("==================================")
#Financial Reports
def generate_report(transactions, month=None):
    if month:
        try:
            date.fromisoformat(month + "-01")
        except ValueError:
            print("Invalid month. Use YYYY-MM.")
            return
        records = [
            t for t in transactions
            if t.date.startswith(month)
        ]
        print(f"\n========== REPORT: {month} ==========")
    else:
        records = transactions
        print("\n========== FINANCIAL REPORT ==========")
    income = sum(t.amount for t in records if t.type == "income")
    expenses = sum(t.amount for t in records if t.type == "expense")
    net = income - expenses
    print(f"Income:   Rs {income:,.2f}")
    print(f"Expenses: Rs {expenses:,.2f}")
    print(f"Net:      Rs {net:,.2f}")
    category_totals = defaultdict(float)
    for transaction in records:
        if transaction.type == "expense":
            category_totals[transaction.category] += transaction.amount
    print("\nExpenses by category:")
    if category_totals:
        for category, amount in sorted(category_totals.items()):
            print(f"  {category}: Rs {amount:,.2f}")
    else:
        print("  No expenses recorded.")
    monthly_totals = defaultdict(lambda: {
        "income": 0,
        "expenses": 0
    })
    for transaction in records:
        month_key = transaction.date[:7]
        if transaction.type == "income":
            monthly_totals[month_key]["income"] += transaction.amount
        else:
            monthly_totals[month_key]["expenses"] += transaction.amount
    print("\nMonthly summary:")
    if monthly_totals:
        for month_key in sorted(monthly_totals):
            values = monthly_totals[month_key]
            print(
                f"  {month_key}: "
                f"Income Rs {values['income']:,.2f} | "
                f"Expenses Rs {values['expenses']:,.2f} | "
                f"Net Rs {values['income'] - values['expenses']:,.2f}"
            )
    else:
        print("  No monthly data available.")
    expense_records = [
        t for t in records if t.type == "expense"
    ]
    if expense_records:
        biggest = max(expense_records, key=lambda t: t.amount)
        print("\nBiggest expense:")
        print(
            f"  Rs {biggest.amount:,.2f} - "
            f"{biggest.category} ({biggest.description})"
        )
    else:
        print("\nNo expenses recorded.")
    print("=====================================")
#Help Menu
def show_help():
    print("""
Available Commands:
1. Add Income:
   add income 40000 Salary "July salary"

2. Add Expense:
   add expense 250 Food "Lunch"

3. Add with custom date:
   add expense 500 Travel "Bus ticket" 2026-07-15

4. List Transactions:
   list

5. Financial Report:
   report

6. Monthly Report:
   report 2026-07

7. Help:
   help

8. Exit:
   quit

Amount must be positive.
Date format: YYYY-MM-DD
""")

#Command Processing
def process_command(command, transactions):
    try:
        parts = shlex.split(command)
        if not parts:
            return True
        action = parts[0].lower()
        if action == "add":
            add_transaction(transactions, parts)
        elif action == "list":
            list_transactions(transactions)
        elif action == "report":
            if len(parts) > 2:
                print("Usage: report [YYYY-MM]")
            else:
                month = parts[1] if len(parts) == 2 else None
                generate_report(transactions, month)
        elif action == "help":
            show_help()
        elif action in ("quit", "exit"):
            print("Goodbye! Your financial data is saved.")
            return False
        else:
            print("Unknown command. Type 'help' for instructions.")
    except ValueError as error:
        print(f"Invalid input: {error}")
    return True

#Main Application
def main():
    transactions = load_transactions()
    print("\n================================")
    print("     PERSONAL FINANCE TRACKER")
    print("================================")
    print(f"Loaded {len(transactions)} transaction(s).")
    print("Type 'help' to see available commands.")
    running = True
    while running:
        try:
            command = input("\n> ").strip()
            running = process_command(command, transactions)
        except KeyboardInterrupt:
            print("\nUse 'quit' to exit safely.")
        except EOFError:
            print("\nGoodbye!")
            break
        except Exception as error:
            print(f"Something went wrong: {error}")

if __name__ == "__main__":
    main()