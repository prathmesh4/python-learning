# Import classes from models.py.
from models import Student, Teacher
# Import utility functions from utils.py.
from utils import validate_marks, format_grade
# Creating at least 3 student objects.
students = [
    Student("Prathmesh", 20, 101, 85),
    Student("pranv", 21, 102, 92),
    Student("Amit", 19, 103, 76)
]
# Creating at least 2 teacher objects.
teachers = [
    Teacher("Mr. Sawant", 40, "Python", 50000),
    Teacher("Mrs. Patil", 35, "Mathematics", 45000)
]
# Display student information.
print("===== STUDENT DETAILS =====")
for student in students:
    print(student.display())
    # Use utility function to validate marks.
    if validate_marks(student.marks):
        print("Marks are valid")
        print(format_grade(
            "A" if student.marks >= 90
            else "B" if student.marks >= 80
            else "C"
        ))
    else:
        print("Invalid marks")
    print()
# Display teacher information.
print("===== TEACHER DETAILS =====")
for teacher in teachers:
    print(teacher.display())

"""First Split
Moving classes into separate files with proper imports
Take the Student and Teacher classes (with Person base class) from earlier sections. Split into 3 files:


project/
├── models.py     — Person, Student, Teacher classes
├── utils.py      — validate_marks(marks) returns True/False, format_grade(grade) returns formatted string
└── main.py       — imports from both files, creates objects, runs the program

Requirements:
- models.py should have a if __name__ == "__main__" block that tests the classes when run directly
- utils.py should also have a test block
- main.py imports from both and creates at least 3 students and 2 teachers, displays them, and uses util functions

Verify:
1. python models.py runs tests
2. python utils.py runs tests
3. python main.py runs the program WITHOUT showing test output from models or utils

Describe in comments: why did you put each piece where you did?
"""