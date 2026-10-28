p=float(input("Loan Amount: "))
annual_rate=float(input("Annual Interest rate (%): "))
n=float(input("Tenure (months): "))

r=(annual_rate/12)/100
emi = p * r * (1 + r)**n / ((1 + r)**n -1)

print("Monthly EMI: RS",round(emi,2))

"""EMI Calculator
Multiple inputs feeding a real-world formula
Ask the user for a loan amount, an annual interest rate (percent), and a tenure in months. Compute the monthly EMI (equated monthly instalment).

Formula:

r = (annual_rate / 12) / 100          # monthly rate as a decimal
EMI = P * r * (1 + r)**n / ((1 + r)**n - 1)
where P is the loan amount and n is the number of months.

Print the EMI rounded to 2 decimal places.

Example:

Loan amount: 500000
Annual interest rate (%): 8.5
Tenure (months): 60
Monthly EMI: Rs 10258.27
"""