full_name = input("Full name: ").strip()
names = full_name.split()
first_name = names[0]
last_name = names[-1]

initials = ".".join(name[0].upper() for name in names) + "."

title_case = full_name.title()

print("First:", first_name)
print("Last:", last_name)
print("Initials:", initials)
print("Title Case:", title_case)