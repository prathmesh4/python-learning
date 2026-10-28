principal=1000
rate=5
time=2

simple_interest=(principal * rate * time)/100
total_amount=principal + simple_interest
print("Simple Interest :",simple_interest)
print("Total Amount :",total_amount)

"""Simple Interest Calculator
Storing values in variables and reusing them
Build a simple interest calculator driven by variables.

Define three variables: principal, rate (percent per year), and time (in years). Then calculate:
• Simple Interest:  SI = (principal × rate × time) / 100
• Total amount:     principal + SI

Print both results with a clear label.

Example (principal = 1000, rate = 5, time = 2):

Simple Interest: 100.0
Total Amount: 1100.0

Now change principal to a new value at the top and run again — notice that only ONE line changes, but both results update. That is the whole point of variables."""