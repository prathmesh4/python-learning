# Import from the public library package API.
from library import Book, Member, Library
# Import reusable validation functions.
from library.utils import validate_isbn, validate_member_id

def find_book(library, isbn):
    return next(
        (book for book in library.books if book.isbn == isbn),
        None
    )
def find_member(library, member_id):
    return next(
        (
            member for member in library.members
            if member.member_id == member_id
        ),
        None
    )
def add_new_book(library):
    title = input("Enter book title: ").strip()
    author = input("Enter author: ").strip()
    isbn = input("Enter ISBN: ").strip()
    if not title or not author:
        print("Error: Title and author are required.")
        return
    if not validate_isbn(isbn):
        print("Error: Invalid ISBN.")
        return
    book = Book(title, author, isbn)
    try:
        library.add_book(book)
        print("Book added successfully!")
    except ValueError as error:
        print("Error:", error)
def register_member(library):
    name = input("Enter member name: ").strip()
    member_id = input("Enter member ID: ").strip()
    if not name:
        print("Error: Name is required.")
        return
    if not validate_member_id(member_id):
        print("Error: Invalid member ID.")
        return
    member = Member(name, member_id)
    try:
        library.register_member(member)
        print("Member registered successfully!")
    except ValueError as error:
        print("Error:", error)
def borrow_a_book(library):
    member_id = input("Enter member ID: ").strip()
    isbn = input("Enter book ISBN: ").strip()
    member = find_member(library, member_id)
    book = find_book(library, isbn)
    if member is None:
        print("Error: Member not found.")
        return
    if book is None:
        print("Error: Book not found.")
        return
    try:
        transaction = library.borrow_book(member, book)
        print("Book borrowed successfully!")
        print(transaction)
    except (ValueError, TypeError) as error:
        print("Error:", error)
def return_a_book(library):
    member_id = input("Enter member ID: ").strip()
    isbn = input("Enter book ISBN: ").strip()
    member = find_member(library, member_id)
    book = find_book(library, isbn)
    if member is None:
        print("Error: Member not found.")
        return
    if book is None:
        print("Error: Book not found.")
        return
    try:
        fine = library.return_book(member, book)
        print("Book returned successfully!")
        print(f"Fine: Rs. {fine}")
    except (ValueError, TypeError) as error:
        print("Error:", error)
def search_books(library):
    print("\n1. Search by title")
    print("2. Search by author")
    choice = input("Choose search type: ").strip()
    if choice == "1":
        query = input("Enter title: ").strip()
        results = library.search_by_title(query)
    elif choice == "2":
        query = input("Enter author: ").strip()
        results = library.search_by_author(query)
    else:
        print("Invalid search option.")
        return
    if results:
        print("\nSearch Results:")
        for book in results:
            print(book)
    else:
        print("No books found.")
def display_books(library):
    print("\n===== ALL BOOKS =====")
    if not library.books:
        print("No books in library.")
        return
    for book in library.books:
        print(book)
def display_members(library):
    print("\n===== ALL MEMBERS =====")
    if not library.members:
        print("No registered members.")
        return
    for member in library.members:
        print(member)
def main():
    library = Library()
    try:
        if library.load():
            print("Previous library data loaded.")
        else:
            print("Starting a new library.")
    except (OSError, ValueError, KeyError, TypeError) as error:
        print(f"Could not load saved library data: {error}")
        print("Starting with an empty library.")
    while True:
        print("\n========== LIBRARY MANAGEMENT ==========")
        print("1. Add Book")
        print("2. Register Member")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Search Books")
        print("6. Display All Books")
        print("7. Display All Members")
        print("8. Save and Exit")
        choice = input("\nEnter your choice: ").strip()
        try:
            if choice == "1":
                add_new_book(library)
            elif choice == "2":
                register_member(library)
            elif choice == "3":
                borrow_a_book(library)
            elif choice == "4":
                return_a_book(library)
            elif choice == "5":
                search_books(library)
            elif choice == "6":
                display_books(library)
            elif choice == "7":
                display_members(library)
            elif choice == "8":
                library.save()
                print("Library data saved successfully.")
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
        except (OSError, ValueError, TypeError) as error:
            print("Operation failed:", error)
        except KeyboardInterrupt:
            print("\nOperation cancelled.")
    return

# Application entry point.
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nApplication interrupted.")


"""Library Management Package
Full package structure with __init__.py public APIs, cross-module imports, and clean architecture
Refactor a Library Management System into a proper Python package.

Package structure:

library/
├── __init__.py                — public API: from library import Book, Member, Library
├── models/
│   ├── __init__.py            — from .book import Book; from .member import Member
│   ├── book.py                — Book class (title, author, isbn, is_available)
│   ├── member.py              — Member class (name, member_id, borrowed_books list)
│   └── transaction.py         — BorrowTransaction class (book, member, borrow_date, due_date)
├── services/
│   ├── __init__.py
│   ├── catalog.py             — search_by_title(), search_by_author(), add_book(), remove_book()
│   └── checkout.py            — borrow_book(), return_book(), calculate_fine()
├── utils/
│   ├── __init__.py
│   └── validators.py          — validate_isbn(), validate_member_id()
└── data/
    └── library_data.json      — persistence file

Separate from the package:

main.py                        — menu-driven program that uses the library package
requirements.txt

Requirements:
1. Each module is independently importable: from library.models import Book works
2. The top-level library/__init__.py provides a clean public API so users can also do from library import Book, Member
3. No circular imports — think about dependency direction
4. Models use proper OOP: Book should have __str__, __repr__, __eq__ (by ISBN)
5. Services take objects as parameters, not raw data — borrow_book(member, book) not borrow_book(member_id, isbn)
6. Persistence: save/load library state to/from JSON file
7. Include a if __name__ == "__main__" test block in at least 2 modules
8. main.py should be a working menu-driven program: add book, register member, borrow, return, search, display all, save & exit

This is a system design exercise as much as a coding exercise. Think about which module depends on which, and make sure dependencies flow ONE direction (models know nothing about services, services know about models, main knows about both).
"""