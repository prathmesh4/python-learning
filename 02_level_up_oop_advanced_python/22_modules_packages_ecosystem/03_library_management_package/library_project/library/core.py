import json
from pathlib import Path
from datetime import datetime
from library.models import Book, Member, BorrowTransaction
from library.services.catalog import (
    add_book,
    remove_book,
    search_by_title,
    search_by_author
)
from library.services.checkout import (
    borrow_book,
    return_book
)

class Library:
    def __init__(self, data_file=None):
        self.data_file = (
            Path(data_file)
            if data_file
            else Path(__file__).parent / "data" / "library_data.json"
        )
        self.books = []
        self.members = []
        self.transactions = []
    def add_book(self, book):
        return add_book(self.books, book)
    def remove_book(self, book):
        return remove_book(self.books, book)
    def register_member(self, member):
        if not isinstance(member, Member):
            raise TypeError("Expected a Member object")
        if any(
            m.member_id == member.member_id
            for m in self.members
        ):
            raise ValueError("Member ID already exists")
        self.members.append(member)
        return True
    def borrow_book(self, member, book, days=14):
        return borrow_book(
            member,
            book,
            self.transactions,
            days
        )
    def return_book(self, member, book):
        return return_book(
            member,
            book,
            self.transactions
        )
    def search_by_title(self, title):
        return search_by_title(self.books, title)
    def search_by_author(self, author):
        return search_by_author(self.books, author)
    def save(self):
        """Save library state to JSON."""
        self.data_file.parent.mkdir(
            parents=True,
            exist_ok=True
        )
        data = {
            "books": [
                {
                    "title": book.title,
                    "author": book.author,
                    "isbn": book.isbn,
                    "is_available": book.is_available
                }
                for book in self.books
            ],
            "members": [
                {
                    "name": member.name,
                    "member_id": member.member_id
                }
                for member in self.members
            ],
            "transactions": [
                {
                    "isbn": t.book.isbn,
                    "member_id": t.member.member_id,
                    "borrow_date": t.borrow_date.isoformat(),
                    "due_date": t.due_date.isoformat()
                }
                for t in self.transactions
            ]
        }
        with self.data_file.open("w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
    def load(self):
        """Load library state from JSON."""
        if not self.data_file.exists():
            return False
        with self.data_file.open("r", encoding="utf-8") as file:
            data = json.load(file)
        books = [
            Book(
                item["title"],
                item["author"],
                item["isbn"],
                item["is_available"]
            )
            for item in data.get("books", [])
        ]
        book_by_isbn = {
            book.isbn: book for book in books
        }
        members = [
            Member(
                item["name"],
                item["member_id"]
            )
            for item in data.get("members", [])
        ]
        member_by_id = {
            member.member_id: member for member in members
        }
        transactions = []
        for item in data.get("transactions", []):
            book = book_by_isbn.get(item["isbn"])
            member = member_by_id.get(item["member_id"])
            if book is None or member is None:
                raise ValueError("Invalid transaction in saved data")
            transaction = BorrowTransaction(
                book,
                member,
                datetime.fromisoformat(item["borrow_date"]),
                datetime.fromisoformat(item["due_date"])
            )
            transactions.append(transaction)
            member.borrow(book)
        self.books = books
        self.members = members
        self.transactions = transactions
        return True
if __name__ == "__main__":
    library = Library()
    library.load()
    print("Library initialized.")
    print("Books:", len(library.books))
    print("Members:", len(library.members))