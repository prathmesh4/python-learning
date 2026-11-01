from library.models import Book

def add_book(books, book):
    """Add a Book object to the catalog."""
    if not isinstance(book, Book):
        raise TypeError("Expected a Book object")
    if book in books:
        raise ValueError("Book already exists")
    books.append(book)
    return True
def remove_book(books, book):
    """Remove a Book object from the catalog."""
    if not isinstance(book, Book):
        raise TypeError("Expected a Book object")
    if book not in books:
        raise ValueError("Book not found")
    if not book.is_available:
        raise ValueError("Cannot remove a borrowed book")
    books.remove(book)
    return True
def search_by_title(books, title):
    """Search books by title."""
    return [
        book for book in books
        if title.lower() in book.title.lower()
    ]
def search_by_author(books, author):
    """Search books by author."""
    return [
        book for book in books
        if author.lower() in book.author.lower()
    ]

if __name__ == "__main__":
    books = []
    book = Book(
        "Python Basics",
        "John Smith",
        "9780132350884"
    )
    add_book(books, book)
    print(search_by_title(books, "Python"))
    print(search_by_author(books, "John"))