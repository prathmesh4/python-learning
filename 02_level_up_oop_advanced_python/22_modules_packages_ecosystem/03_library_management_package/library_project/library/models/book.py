class Book:
    def __init__(self, title, author, isbn, is_available=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = is_available
    def __str__(self):
        status = "Available" if self.is_available else "Borrowed"

        return (
            f"{self.title} by {self.author} "
            f"(ISBN: {self.isbn}) - {status}"
        )
    def __repr__(self):
        return (
            f"Book(title={self.title!r}, "
            f"author={self.author!r}, "
            f"isbn={self.isbn!r})"
        )
    def __eq__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return self.isbn == other.isbn
if __name__ == "__main__":
    book1 = Book("Python Basics", "John Smith", "1234567890")
    book2 = Book("Python Advanced", "Jane Doe", "1234567890")
    print(book1)
    print(repr(book1))
    print("Are books equal?", book1 == book2)