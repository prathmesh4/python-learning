import re
password=input("Password: ")

length_ok= len(password) >= 8
lowercase_ok = password.lower() != password
uppercase_ok = password.upper()!= password
digit_ok = bool(re.search(r"[0-9]", password))
special_ok = bool(re.search(r"[!@#$%^&*]", password))

score = sum([length_ok, uppercase_ok, lowercase_ok, digit_ok, special_ok])

print("Length >= 8:  ", "Yes" if length_ok else "No")
print("Uppercase:    ", "Yes" if uppercase_ok else "No")
print("Lowercase:    ", "Yes" if lowercase_ok else "No")
print("Digit:        ", "Yes" if digit_ok else "No")
print("Special char: ", "Yes" if special_ok else "No")

strength = "Weak" if score <= 2 else "Medium" if score <= 4 else "Strong"

print(f"Strength: {strength} ({score}/5)")

"""Password Strength Checker
String checks without loops
Ask for a password and rate its strength by checking 5 criteria:
• At least 8 characters long
• Contains an uppercase letter
• Contains a lowercase letter
• Contains a digit
• Contains a special character (one of !@#$%^&*)

Count how many criteria pass and rate it: 0–2 Weak, 3–4 Medium, 5 Strong. Print a checklist showing which criteria passed. Use only the "in" operator and string methods — no loops.

Example:

Password: Tab47!
Length >= 8:   No
Uppercase:     Yes
Lowercase:     Yes
Digit:         Yes
Special char:  Yes
Strength: Medium (4/5)
"""