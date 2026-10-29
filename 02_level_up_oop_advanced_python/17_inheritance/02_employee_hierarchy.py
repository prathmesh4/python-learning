class Person:
    def __init__(self,name , age):
        self.name=name
        self.age=age
    def display(self):
        print(f"Name: {self.name}, Age={self.age}")
class Employee(Person):
    def __init__(self, name, age,emp_id, base_salary):
        super().__init__(name, age)            
        self.emp_id=emp_id
        self.base_salary=base_salary
    def calculate_pay(self):
        return self.base_salary
class Developer(Employee):
    def __init__(self, name, age, emp_id, base_salary,language,overtime_hours):
        super().__init__(name, age, emp_id, base_salary)        
        self.language=language
        self.overtime_hours=overtime_hours
    def calculate_pay(self):
        return self.base_salary + (self.overtime_hours * 500)    
class Manager(Employee):
    def __init__(self, name, age, emp_id, base_salary,department, team_size):
        super().__init__(name, age, emp_id, base_salary)        
        self.department=department
        self.team_size=team_size
    def calculate_pay(self):
        return self.base_salary + (self.team_size * 2000)
class Intern(Employee):
    def __init__(self, name, age, emp_id, base_salary,stipend, duration_months):
        super().__init__(name, age, emp_id, base_salary)        
        self.stipend=stipend
        self.duration_months = duration_months
    def calculate_pay(self):
        return self.stipend    
class Department:
    def __init__(self,name):
        self.name=name
        self.employees=[]
    def add_employee(self,employee   ):
        self.employees.append(employee) 
    def total_payroll(self):
        return sum(emp.calculate_pay() for emp in  self.employees)    
    def average_salary(self):
        if not self.employees:
            return 0
        return self.total_payroll()/ len(self.employees)
    def display_report(self):
        print(f"{self.name} Departmnet Report:")
        print(f"{'Name':<16} {'Type':<13} {'Pay':>12}")
        print("-" *41)
        for emp in self.employees:
            emp_type= type(emp).__name__
            pay= emp.calculate_pay()
            print(f"{emp.name:<16} {emp_type:<13}RS {pay:>8,}")
        print("-" *41)
        print(f"Total Payroll: Rs {self.total_payroll():,}")
        print(f"Average Salary: Rs {self.average_salary():,.2f}")
engineering=Department("Engineering")
engineering.add_employee(Developer("Prathmeh",30,"E001",50000,"Python",25))            
engineering.add_employee(Manager("Prathm",32,"E002",40000,"Engineering",10))            
engineering.add_employee(Developer("Rahul", 26, "E103", 45000, "Java", 20))
engineering.add_employee(Intern("Sara", 21, "E104", 30000, 15000, 6))
engineering.add_employee(Manager("Neha", 40, "E105", 70000, "Platform", 8))
engineering.add_employee(Developer("Karan", 30, "E106", 55000, "C++", 15))
engineering.add_employee(Intern("Meera", 22, "E107", 25000, 12000, 3))
engineering.add_employee(Developer("Arjun", 29, "E108", 48000, "Python", 10))      
engineering.display_report()            

"""Employee Hierarchy
Multi-level inheritance with different behavior per subclass
Build an employee system with inheritance:

Base class: Person
- Attributes: name, age
- Method: display()

Child: Employee(Person)
- Additional attributes: emp_id, base_salary
- Method: calculate_pay() returns base_salary

Grandchildren (inherit from Employee):
- Developer — additional: language, overtime_hours. calculate_pay() = base_salary + (overtime_hours × 500)
- Manager — additional: department, team_size. calculate_pay() = base_salary + (team_size × 2000)
- Intern — additional: stipend, duration_months. calculate_pay() = stipend (ignores base_salary)

Create a Department class (NOT inheriting from anything — this is composition):
- Holds a list of Employee objects
- Methods: total_payroll(), average_salary(), display_report()

Create at least 8 employees across all types. Print the department report.

Example output:

Engineering Department Report:
Name            Type         Pay
Amit            Developer    Rs 62,500
Priya           Manager      Rs 80,000
Rahul           Developer    Rs 55,000
Sara            Intern       Rs 15,000
...

Total Payroll: Rs 4,50,000
Average Salary: Rs 56,250
"""