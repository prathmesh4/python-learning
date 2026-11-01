class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def displat(self):
        return f"Name: {self.name}, Age: {self.age}" 
class Student(Person):
    def __init__(self,name,age,roll_no,marks):
        super().__init__(name,age)
        self.roll_no=roll_no
        self.marks=marks
    def display(self):
        return (
            f"Student: {self.name}, Age: {self.age}, "
            f"Roll No: {self.roll_no}, Marks: {self.marks}"
        )
class Teacher(Person):
    def __init__(self, name, age,subject,salary):
        super().__init__(name, age)            
        self.subject=subject
        self.salary=salary
    def display(self):
        return (
            f"Teacher: {self.name}, Age: {self.age}, "
            f"Subject: {self.subject}, Salary: {self.salary}"
        )
# This block runs only when models.py is executed directly.
# It does not run when another file imports models.py.        
if  __name__ == "__main__":
    print("Testing models.py...")
    student = Student("Prathmesh", 20, 101, 85)
    teacher = Teacher("Mr. Sawant", 40, "Python", 50000)
    print(student.display())
    print(teacher.display())