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