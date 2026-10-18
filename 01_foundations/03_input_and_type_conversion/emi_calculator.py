p=float(input("Loan Amount: "))
annual_rate=float(input("Annual Interest rate (%): "))
n=float(input("Tenure (months): "))

r=(annual_rate/12)/100
emi = p * r * (1 + r)**n / ((1 + r)**n -1)

print("Monthly EMI: RS",round(emi,2))