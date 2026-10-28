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

"""Name Formatter
Slicing and string methods
Ask for a full name and produce:
• The first name and last name separately
• The initials (e.g. "Rahul Kumar Sharma" -> "R.K.S.")
• The name in Title Case

Handle names of any length — two words, three words, or more.

Example:

Full name: Prathmesh Ravindra Sawant
First: Prathmesh
Last: Sawant
Initials: P.R.S.
Title Case: Prathmesh Ravindra Sawant

Hint: split() turns the name into a list of words you can index and loop over.
"""