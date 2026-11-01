from datetime import datetime
from library.models import Book, Member, BorrowTransaction

def borrow_book(member, book, transactions, days=14):
    """Borrow a Book object for a Member object."""
    if not isinstance(member, Member):
        raise TypeError("Expected a Member object")
    if not isinstance(book, Book):
        raise TypeError("Expected a Book object")
    if not book.is_available:
        raise ValueError("Book is not available")
    if book in member.borrowed_books:
        raise ValueError("Member already borrowed this book")
    from datetime import timedelta
    borrow_date = datetime.now()
    transaction = BorrowTransaction(
        book,
        member,
        borrow_date,
        borrow_date + timedelta(days=days)
    )
    book.is_available = False
    member.borrow(book)
    transactions.append(transaction)
    return transaction

def return_book(member, book, transactions):
    """Return a borrowed Book object."""
    if not isinstance(member, Member):
        raise TypeError("Expected a Member object")
    if not isinstance(book, Book):
        raise TypeError("Expected a Book object")
    if book not in member.borrowed_books:
        raise ValueError("This member has not borrowed this book")
    transaction = next(
        (
            t for t in reversed(transactions)
            if t.member.member_id == member.member_id
            and t.book.isbn == book.isbn
        ),
        None
    )
    if transaction is None:
        raise ValueError("Borrow transaction not found")
    fine = calculate_fine(transaction)
    member.return_book(book)
    book.is_available = True
    transactions.remove(transaction)
    return fine

def calculate_fine(transaction, daily_rate=5, today=None):
    """Calculate overdue fine in rupees."""
    today = today or datetime.now()
    overdue_days = max(
        0,
        (today.date() - transaction.due_date.date()).days
    )
    return overdue_days * daily_rate

if __name__ == "__main__":
    from library.models import Book, Member
    books = []
    transactions = []
    book = Book(
        "Python Basics",
        "John Smith",
        "9780132350884"
    )
    member = Member("Rahul", "M001")
    books.append(book)
    transaction = borrow_book(member, book, transactions)
    print(transaction)
    print("Fine:", calculate_fine(transaction))