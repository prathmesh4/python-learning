class Money:
    def __init__(self,amount:float,currency:str):
        self.amount=amount
        self.currency=currency
    def __str__(self):
        if self.currency=="INR":
            return f"Rs {self.amount:,.2f}"    
        elif self.currency=="USD":
            return f"$ {self.amount:,.2f}"    
        return f"{self.currency} {self.amount:,.2f}"    
    def __repr__(self):
        return f"Money {self.amount:.2f} '{self.currency}'"
    def __eq__(self, value):
        if not isinstance(value,Money):
            return NotImplemented
        return (
            self.amount == value.amount
            and self.currency == value.currency
        )
    def __lt__(self, other):
        if not isinstance(other,Money):
            return NotImplemented    
        if self.currency !=other.currency:
            raise ValueError(f"Can not compare {self.currency} and {other.currency}")
        return self.amount < other.amount
    def __add__(self, other):
        if not isinstance(other,Money):
            return NotImplemented    
        if self.currency !=other.currency:
            raise ValueError(f"Can not compare {self.currency} and {other.currency}")
        return Money( self.amount + other.amount,self.currency)
m1=Money(1500,"INR")    
m2=Money(2000,"INR")    
m3=Money(500,"INR")    
usd=Money(100,"USD")    
print(m1)
print([m1,m2])
print(f"{m1} == {Money(1500,'INR')}: {m1 == Money(1500,'INR')}")
print(f"{m1} < {m2}: {m1 < m2}")
total= m1+m2
print(f"{m1} + {m2}: {total}")
money_list=[m3,m2,m1]
print("Sorted:",money_list.sort())
try:
    print(m1 + usd)
except ValueError as e:
    print("Adding INR + USD:")
    print(f"ValueError:{e}")    
try:
    print(m1 < usd)
except ValueError as e:
    print("Comparing INR < USD:")
    print(f"ValueError: {e}")    


"""Money Class
You'll practice
String representation, comparison, and arithmetic with dunder methods
Create a Money class with amount (float) and currency (string, e.g., "INR", "USD").

Implement the following dunder methods:
- __str__ — returns human-readable format: "Rs 1,500.00" for INR, "$1,500.00" for USD
- __repr__ — returns developer format: "Money(1500.00, 'INR')"
- __eq__ — two Money objects are equal if same amount AND same currency
- __lt__ — compare amounts (only if same currency — raise ValueError if currencies differ)
- __add__ — add two Money objects (only if same currency — raise ValueError if different). Returns a new Money object.

Demonstrate:
1. Print a Money object (should use __str__)
2. Put a Money object in a list and print the list (should use __repr__)
3. Compare two Money objects with same currency
4. Sort a list of Money objects
5. Add two Money objects
6. Try adding/comparing Money with different currencies — show the error

Example output:

Rs 1,500.00
[Money(1500.00, 'INR'), Money(2000.00, 'INR')]
Rs 1,500.00 == Rs 1,500.00: True
Rs 1,500.00 < Rs 2,000.00: True
Rs 1,500.00 + Rs 2,000.00 = Rs 3,500.00
Sorted: [Rs 500.00, Rs 1,500.00, Rs 2,000.00]

Adding INR + USD:
ValueError: Cannot add INR and USD
"""
    