class Employee:
    caompany_name="Tab 47"
    employee_count=0
    
    def __init__(self,name,emp_id,email,department):
        self.name=name
        self.emp_id=emp_id
        self.email=email
        self.department=department
        
        Employee.employee_count +=1 
    
    @classmethod
    def form_dict(cls,data):
        return cls(
            data["name"],
            data["emp_id"],
            data["email"],
            data["department"]
        )
    
    @classmethod
    def form_csv_line(cls,line):
        name,emp_id,email,department =line.strip().split(",")
        return cls(name,emp_id,email,department)
    @staticmethod
    def is_valid_email(email):
        if not isinstance(email, str) or '@' not in email:
            return False
        local_part, domain =email.split("@",1)
        return(
            bool(local_part)
            and "." in domain
            and bool(domain.split(".",1)[0])
            and bool(domain.split(".",1)[1])
        )
    def display(self):
        print(
            f"[{self.caompany_name}]  {self.name}"
            f"({self.emp_id}) - {self.department} - {self.email}"
        )    

emp = Employee(
    "Prathmesh",
    "E001",
    "Prathmesh@tab47.com",
    "Engineering"
)      
employee_data  ={
    "name":"pranv",
    "emp_id":"E002",
    "email":"pranav@tab47.com",
    "department":"Design"
}
empdict=Employee.form_dict(employee_data)
empcsv=Employee.form_csv_line("dilip,E003,dilip@tab47.com,Marketing")

employees=[emp,empdict,empcsv]
for e in employees:
    e.display()
print(f"Total employee count ; {Employee.employee_count}")
print(
    f'is_valid_email("Prathmesh@tab47.com")'
    f'{Employee.is_valid_email("Prathmesh@tab47.com")}'
)
print(
    f'is_valid_email("invalid-email")'
    f'{Employee.is_valid_email("invalid-email")}'
)    

"""Employee Factory
Alternative constructors with @classmethod — creating objects from different data formats
Create an Employee class with:

Class attributes:
- company_name = "Tab47 Inc"
- employee_count — auto-increments on each creation

Instance attributes:
- name, emp_id, email, department

Three ways to create an Employee (class methods):
- Standard __init__(name, emp_id, email, department)
- from_dict(data) — creates from a dictionary like {"name": "Amit", "emp_id": "E001", "email": "amit@tab47.com", "department": "Engineering"}
- from_csv_line(line) — creates from a CSV string like "Amit,E001,amit@tab47.com,Engineering"

Static method:
- is_valid_email(email) — returns True if email contains "@" and "." after the "@"

Instance method:
- display() — prints all employee info including company name

Create employees using all three methods. Validate emails. Print the total count.

Example output:

[Tab47 Inc] Amit (E001) — Engineering — amit@tab47.com
[Tab47 Inc] Priya (E002) — Design — priya@tab47.com
[Tab47 Inc] Rahul (E003) — Marketing — rahul@tab47.com

Total employees: 3
is_valid_email("amit@tab47.com"): True
is_valid_email("invalid-email"): False"""
