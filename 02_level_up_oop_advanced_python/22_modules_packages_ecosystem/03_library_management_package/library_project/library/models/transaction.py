from datetime import datetime, timedelta

class BorrowTransaction:
    def __init__(
        self,
        book,
        member,
        borrow_date=None,
        due_date=None
    ):
        self.book = book
        self.member = member
        self.borrow_date = (
            borrow_date or datetime.now()
        )
        self.due_date = (
            due_date
            or self.borrow_date + timedelta(days=14)
        )
    def __str__(self):
        return (
            f"{self.member.name} borrowed "
            f"{self.book.title}. "
            f"Due: {self.due_date.strftime('%Y-%m-%d')}"
        )

if __name__ == "__main__":
    from library.models.book import Book
    from library.models.member import Member
    book = Book("Python Basics", "John Smith", "1234567890")
    member = Member("Prathm", "M001")
    transaction = BorrowTransaction(book, member)
    print(transaction)