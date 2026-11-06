
# Personal Finance Tracker

A modular command-line application built with Python to track personal income and expenses.

## Features

- Record income and expenses.
- Assign categories to transactions.
- Store transaction dates.
- Automatically save transactions to JSON.
- Automatically load data on startup.
- Generate financial reports.
- View expenses by category.
- Generate monthly summaries.
- Identify the biggest expense.
- Handle invalid user input gracefully.

## Project Structure

```text
02_personal_finance_tracker/
│
├── models.py
├── storage.py
├── main.py
├── transactions.json
├── requirements.txt
└── README.md
```

## Requirements

- Python 3.8 or newer.
- No external dependencies.

## Installation

1. Navigate to the project directory.

2. Run the application:

   python main.py

3. No additional package installation is necessary.

## Available Commands

### Add Income

```text
add income 40000 Salary "July salary"
```

### Add Expense

```text
add expense 250 Food "Lunch"
```

### Add Transaction with Custom Date

```text
add expense 500 Travel "Bus ticket" 2026-07-15
```

### List Transactions

```text
list
```

### Generate Financial Report

```text
report
```

### Generate Monthly Report

```text
report 2026-07
```

### Help

```text
help
```

### Exit

```text
quit
```

## Data Storage

All transactions are stored in:

`transactions.json`

The application automatically loads existing transactions when it starts.

## Example Report

```text
========== FINANCIAL REPORT ==========

Income:   Rs 40,000.00
Expenses: Rs 250.00
Net:      Rs 39,750.00

Expenses by category:
  Food: Rs 250.00

Monthly summary:
  2026-07: Income Rs 40,000.00 |
  Expenses Rs 250.00 |
  Net Rs 39,750.00

Biggest expense:
  Rs 250.00 - Food (Lunch)

=====================================
```

## Learning Concepts

This project demonstrates:

- Python modules and imports.
- Classes and dataclasses.
- Object-oriented programming.
- Lists and dictionaries.
- JSON serialization.
- File handling with pathlib.
- Exception handling (EAFP).
- Functions and modular design.
- Data aggregation using collections.

## License

Free to use and modify for educational purposes.
