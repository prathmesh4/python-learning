def validate_marks(marks):
    return isinstance(marks,(int,float)) and 0<=marks <=100
def format_grade(grade):
    return f"Grade: {grade}"
# This block runs only when utils.py is executed directly.
if __name__ == "__main__":
    print("Testing utils.py")
    print("Valid marks:", validate_marks(85))
    print("Invalid marks:", validate_marks(120))
    print(format_grade("A"))