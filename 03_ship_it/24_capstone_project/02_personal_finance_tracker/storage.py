import json
from pathlib import Path


# DATA_FILE = (
#     Path("03_ship_it")
#     / "24_capstone_project"
#     / "02_personal_finance_tracker"
#     / "transactions.json"
# )
DATA_FILE = Path(__file__).resolve().parent / "transactions.json"

def load_transactions():
    """Load transactions from JSON."""

    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, list):
            raise ValueError("Transaction data must be a JSON list.")

        from models import Transaction

        transactions = []

        for item in data:
            try:
                transactions.append(Transaction.from_dict(item))
            except (ValueError, TypeError, KeyError) as error:
                print(f"Skipping invalid transaction: {error}")

        return transactions

    except FileNotFoundError:
        return []

    except (json.JSONDecodeError, OSError, ValueError) as error:
        print(f"Warning: Could not load transactions: {error}")
        return []


def save_transactions(transactions):
    """Save transactions using a temporary file."""

    temp_file = DATA_FILE.with_suffix(".tmp")

    try:
        DATA_FILE.parent.mkdir(parents=True, exist_ok=True)

        with temp_file.open("w", encoding="utf-8") as file:
            json.dump(
                [transaction.to_dict() for transaction in transactions],
                file,
                indent=4
            )

        temp_file.replace(DATA_FILE)
        return True

    except OSError as error:
        print(f"Error saving transactions: {error}")

        try:
            temp_file.unlink()
        except OSError:
            pass

        return False