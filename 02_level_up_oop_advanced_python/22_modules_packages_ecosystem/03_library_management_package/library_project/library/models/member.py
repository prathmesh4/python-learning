class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []
    def borrow(self, book):
        if book not in self.borrowed_books:
            self.borrowed_books.append(book)
    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
    def __str__(self):
        return (
            f"Member: {self.name}, "
            f"ID: {self.member_id}, "
            f"Borrowed books: {len(self.borrowed_books)}"
        )

if __name__ == "__main__":
    from library.models.book import Book
    member = Member("Prathmesh", "M001")
    book = Book("Python Basics", "John Smith", "1234567890")
    member.borrow(book)
    print(member)
    print("Borrowed:", member.borrowed_books)