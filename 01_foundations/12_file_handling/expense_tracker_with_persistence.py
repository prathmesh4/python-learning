import json
import os

FILE_NAME = "expenses.json"
if os.path.exists(FILE_NAME):
    with open(FILE_NAME, "r") as file:
        try:
            expenses = json.load(file)
        except json.JSONDecodeError:
            expenses = []
else:
    expenses = []

while True:
    print("===== EXPENSE TRACKER =====")
    print("1. Add expense")
    print("2. View all expenses")
    print("3. View expenses by category")
    print("4. Show total spending")
    print("5. Save and exit")

    choice = input("Enter your choice (1-5): ")
    if choice == "1":
        try:
            amount = float(input("Enter amount (Rs): "))
            if amount <= 0:
                print("Amount must be greater than zero.")
                continue
        except ValueError:
            print("Please enter a valid amount.")
            continue

        category = input("Enter category: ").strip()
        note = input("Enter note: ").strip()
        expenses.append({
            "amount": amount,
            "category": category,
            "note": note
        })
        print("Expense added successfully!")
    elif choice == "2":
        if not expenses:
            print("No expenses recorded yet.")
        else:
            print("--- All Expenses ---")
            for i, expense in enumerate(expenses, start=1):
                print(
                    f"{i}. Rs {expense['amount']:.2f} | "
                    f"{expense['category']} | {expense['note']}"
                )
    elif choice == "3":
        category = input("Enter category to search: ").strip()
        matching = [
            expense for expense in expenses
            if expense["category"].casefold() == category.casefold()
        ]
        if matching:
            print(f"--- Expenses in {category} ---")
            for expense in matching:
                print(
                    f"Rs {expense['amount']:.2f} | "
                    f"{expense['category']} | {expense['note']}"
                )
        else:
            print("No expenses found for this category.")
    elif choice == "4":
        total = sum(expense["amount"] for expense in expenses)
        print(f"Total spending: Rs {total:.2f}")

    elif choice == "5":
        with open(FILE_NAME, "w") as file:
            json.dump(expenses, file, indent=4)
        print(f"Expenses saved to {FILE_NAME}. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 5.")