celsius=float(input("Enter temperature in celsius :"))

fahrenheit=(celsius * 9/5) + 32
kelvin =celsius + 273.15

print(celsius ,"C =",fahrenheit,"F")
print(celsius ,"C =",kelvin,"K")

"""Temperature Converter
Reading input and converting strings to numbers
Ask the user for a temperature in Celsius, then print it in both Fahrenheit and Kelvin.

Formulas:
• Fahrenheit = (C × 9/5) + 32
• Kelvin     = C + 273.15

Remember: input() gives you a string, so convert it with float() before doing any math — otherwise you'll hit the classic type error.

Example:

Enter temperature in Celsius: 37
37.0 C = 98.6 F
37.0 C = 310.15 K
"""