from dataclasses import dataclass, field
from dataclasses import FrozenInstanceError

@dataclass(frozen=True)
class Address:
    street: str
    city: str
    state: str
    pincode: str
@dataclass
class Employee:
    name: str
    emp_id: str
    base_salary: float
    department: str
    address: Address
    bonuses: list = field(default_factory=list)
    tax_bracket: str = field(init=False)
    total_compensation: float = field(init=False)
    def __post_init__(self):
        if not self.name.strip():
            raise ValueError("Employee name cannot be empty")
        if self.base_salary <= 0:
            raise ValueError("Base salary must be positive")
        if self.base_salary < 250000:
            self.tax_bracket = "0%"
        elif self.base_salary < 500000:
            self.tax_bracket = "5%"
        elif self.base_salary < 1000000:
            self.tax_bracket = "20%"
        else:
            self.tax_bracket = "30%"
        self.total_compensation = (
            self.base_salary + sum(self.bonuses)
        )
@dataclass
class Department:
    name: str
    employees: list = field(default_factory=list)
    budget: float = 0.0

    def summary(self):
        total_payroll = sum(
            emp.total_compensation
            for emp in self.employees
        )
        print(f"{self.name} Department:")
        print(f"Employees: {len(self.employees)}")
        print(f"Total Payroll: Rs {total_payroll:,.0f}")
        print(f"Budget: Rs {self.budget:,.0f}")
        if total_payroll <= self.budget:
            print("Status: Within Budget ✓")
        else:
            print("Status: Over Budget ✗")

address1 = Address("MG Road", "Pune", "MH", "411001")
address2 = Address("MG Road", "Pune", "MH", "411001")
print("Address Objects:")
print(address1)
print("\nTrying to modify frozen Address...")
try:
    address1.city = "Mumbai"
except FrozenInstanceError as e:
    print("FrozenInstanceError:", e)
emp1 = Employee("Prathmesh", "E001", 60000.0,"Engineering", address1, [5000])
emp2 = Employee("Priya", "E002", 300000.0,"Engineering", address1, [10000])
emp3 = Employee("Rahul", "E003", 600000.0,"Engineering", address2, [15000])
emp4 = Employee("Neha", "E004", 1200000.0,"Engineering", address2, [20000])
print("Employee Records:")
print(emp1)
print(emp2)
print(emp3)
print(emp4)
print("Tax Brackets:")
for emp in [emp1, emp2, emp3, emp4]:
    print(
        f"{emp.name}: Rs {emp.base_salary:,.0f} "
        f"-> Tax Bracket: {emp.tax_bracket}"
    )
print("Updating Bonuses:")
emp1.bonuses.append(2000)
emp1.total_compensation = (
    emp1.base_salary + sum(emp1.bonuses)
)
print("Employee:", emp1.name)
print("Bonuses:", emp1.bonuses)
print("Updated Total Compensation:", emp1.total_compensation)
engineering = Department(
    name="Engineering",
    budget=300000
)
engineering.employees.extend([
    emp1, emp2, emp3, emp4
])
engineering.summary()
print("Address Equality:")
print(
    'Address("MG Road", "Pune", "MH", "411001") == '
    'Address("MG Road", "Pune", "MH", "411001"):',
    address1 == address2
)
address_set = {address1, address2}
print("Unique addresses in set:", len(address_set))

"""Employee Records with __post_init__
Computed fields, validation in __post_init__, frozen dataclasses, and conversion
Create three dataclasses:

Address (frozen=True — immutable):
- street, city, state, pincode: str
- Since it's frozen, it can be used as a dict key or in sets

Employee dataclass:
- name: str
- emp_id: str
- base_salary: float
- department: str
- address: Address
- bonuses: list = field(default_factory=list)
- tax_bracket: str = field(init=False) — NOT in constructor, computed automatically
- total_compensation: float = field(init=False) — computed automatically

In __post_init__:
- Validate: name must be non-empty, base_salary must be positive
- Compute tax_bracket: "0%" if salary < 250000, "5%" if < 500000, "20%" if < 1000000, "30%" otherwise
- Compute total_compensation: base_salary + sum(bonuses)

Department dataclass:
- name: str
- employees: list = field(default_factory=list)
- budget: float = 0.0

Add a method summary() that prints department name, employee count, total payroll, and whether payroll is within budget.

Demonstrate:
1. Create frozen Address objects — try modifying one to show the error
2. Create employees with different salaries — show auto-computed tax brackets
3. Add bonuses and show updated total_compensation
4. Create a department, add employees, print summary
5. Show that two Address objects with same values are equal (frozen dataclass generates __hash__)

Example output:

Employee(name='Amit', emp_id='E001', base_salary=60000.0, department='Engineering', tax_bracket='0%', total_compensation=65000.0)

Trying to modify frozen Address...
FrozenInstanceError: cannot assign to field 'city'

Address("MG Road", "Pune", "MH", "411001") == Address("MG Road", "Pune", "MH", "411001"): True

Engineering Department:
Employees: 4
Total Payroll: Rs 2,80,000
Budget: Rs 3,00,000
Status: Within Budget ✓
"""