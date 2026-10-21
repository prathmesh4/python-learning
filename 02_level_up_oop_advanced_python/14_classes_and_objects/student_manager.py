class Student:
    def __init__(self, name, marks, city):
        self.name = name
        self.marks = marks
        self.city = city
    def calculate_grade(self):
        if self.marks >= 90:
            return "A+"
        elif self.marks >= 80:
            return "A"
        elif self.marks >= 70:
            return "B"
        elif self.marks >= 60:
            return "C"
        else:
            return "F"
    def display(self):
        print(
            f"{self.name:<14}"
            f"{self.marks:<8}"
            f"{self.city:<12}"
            f"{self.calculate_grade()}"
        )

class StudentManager:
    def __init__(self):
        self.students = []
    def add_student(self, name, marks, city):
        student = Student(name, marks, city)
        self.students.append(student)
    def remove_by_name(self, name):
        for student in self.students:
            if student.name.lower() == name.lower():
                self.students.remove(student)
                print(f"{name} removed successfully.")
                return
        print(f"Warning: Student '{name}' not found.")
    def get_topper(self):
        if not self.students:
            return None
        return max(self.students, key=lambda student: student.marks)
    def get_average(self):
        if not self.students:
            return 0
        return sum(student.marks for student in self.students) / len(self.students)
    def get_students_by_city(self, city):
        return [
            student for student in self.students
            if student.city.lower() == city.lower()
        ]
    def display_all(self):
        print(f"{'Name':<14}{'Marks':<8}{'City':<12}Grade")
        print("-" * 40)
        for student in self.students:
            student.display()

manager = StudentManager()
manager.add_student("Prathmesh", 95, "Mumbai")
manager.add_student("Pranav", 85, "Solapur")
manager.add_student("Amit", 85, "Pune")
manager.add_student("Priya", 92, "Mumbai")
manager.add_student("Rahul", 67, "Delhi")
manager.add_student("Sara", 78, "Pune")
manager.add_student("Karan", 95, "Mumbai")
manager.add_student("Neha", 55, "Delhi")

print("All Students:")
manager.display_all()
topper = manager.get_topper()
if topper:
    print(f"Topper: {topper.name} ({topper.marks})")
print(f"Average: {manager.get_average():.2f}")

pune_students = manager.get_students_by_city("Pune")
names = ", ".join(student.name for student in pune_students)
print(f"Students from Pune: {names}")
print("Removing Rahul...")
manager.remove_by_name("Rahul")
print(f"Students remaining: {len(manager.students)}")
manager.display_all()
print("Trying to remove an unknown student...")
manager.remove_by_name("Rohan")