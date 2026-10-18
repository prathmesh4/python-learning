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