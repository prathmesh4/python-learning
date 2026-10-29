class Address:
    def __init__(self,street,city,state,pincode):
        self.street=street
        self.city =city
        self.state = state
        self.pincode=pincode
    def display(self):
        return f"{self.street}, {self.city}, {self.state} - {self.pincode}"
    def __str__(self):
        return self.display()
class Person:
    def __init__(self,name,age,address):
        self.name=name
        self.age =age
        self.address=address
    def change_address(self,new_address):
        self.address=new_address
    def display(self):
        print(f"{self.name} , Age {self.age}")
        print(f"Address: {self.address}")    
address1 = Address("42 MG Road", "Pune", "Maharashtra", "411001")
address2 = Address("15 Marine Drive", "Mumbai", "Maharashtra", "400001")
person = Person("Prathmesh", 30, address1)
person.display()
print("\nChanging address...\n")
person.change_address(address2)
person.display()

"""Person with Address
Basic composition — one object containing another
Create two classes: Address and Person.

Address class:
- Attributes: street, city, state, pincode
- Method: display() — returns formatted address string
- Method: __str__ — same as display

Person class:
- Attributes: name, age, address (an Address object — NOT inheriting from Address)
- Method: change_address(new_address) — replaces the address
- Method: display() — prints person info AND their address

Demonstrate:
1. Create 2 Address objects
2. Create a Person with the first address
3. Display the person (should show both person info and address)
4. Change the person's address to the second one
5. Display again — should show updated address

Example output:

Amit, Age 25
Address: 42 MG Road, Pune, Maharashtra — 411001

Changing address...

Amit, Age 25
Address: 15 Marine Drive, Mumbai, Maharashtra — 400001
"""