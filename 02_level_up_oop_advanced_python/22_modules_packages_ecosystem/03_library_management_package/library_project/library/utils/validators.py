import re

def validate_isbn(isbn):
    """
    Validate ISBN-10 or ISBN-13 using check digits.
    Hyphens and spaces are ignored.
    """
    isbn = re.sub(r"[-\s]", "", str(isbn))
    if len(isbn) == 10:
        if not re.fullmatch(r"\d{9}[\dX]", isbn):
            return False
        total = sum(
            (10 - i) * (10 if char == "X" else int(char))
            for i, char in enumerate(isbn)
        )
        return total % 11 == 0
    if len(isbn) == 13:
        if not isbn.isdigit():
            return False
        total = sum(
            int(char) * (1 if i % 2 == 0 else 3)
            for i, char in enumerate(isbn)
        )
        return total % 10 == 0
    return False
def validate_member_id(member_id):
    """
    Member ID must contain at least one letter or digit
    and may contain letters, digits, hyphens and underscores.
    """
    return bool(
        re.fullmatch(r"[A-Za-z0-9_-]{3,20}", str(member_id))
    )
if __name__ == "__main__":
    print("Testing validators")
    print(validate_isbn("9780132350884"))
    print(validate_isbn("1234567890"))
    print(validate_member_id("MEM001"))
    print(validate_member_id("!!"))