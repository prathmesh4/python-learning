class User:
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        value = value.strip()
        if len(value) < 2:
            raise ValueError("Name must be at least 2 characters")
        self._name = value
    @property
    def email(self):
        return self._email
    @email.setter
    def email(self, value):
        if not isinstance(value, str):
            raise TypeError("Email must be a string")
        value = value.lower()
        at_index = value.find("@")
        if at_index == -1 or "." not in value[at_index + 1:]:
            raise ValueError("Invalid email format")
        self._email = value
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, value):
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("Age must be an integer")
        if not 0 <= value <= 150:
            raise ValueError("Age must be between 0 and 150")
        self._age = value
    @property
    def is_adult(self):
        return self.age >= 18

user = User("Pratmesh", "prathmesh@email.com", 30)
print(
    f"User: {user.name}, {user.email}, "
    f"Age {user.age} (Adult: {user.is_adult})"
)

print('Setting email to "Prnav@GMAIL.COM"...')
user.email = "Pranv@GMAIL.COM"
print(f"Stored as: {user.email}")
print('Setting name to "  Rahul  "...')
user.name = "  Rahul  "
print(f"Stored as: {user.name}")
print("Invalid cases:")
tests = [
    ("name", "", ValueError),
    ("email", "invalid", ValueError),
    ("age", -5, ValueError),
    ("age", "hello", TypeError),
    ("age", 200, ValueError),
]
for attribute, value, error_type in tests:
    try:
        setattr(user, attribute, value)
    except (ValueError, TypeError) as e:
        print(f'{attribute} = {value!r}: Error — {e}')
print("Adulthood checks:")
teen = User("Riya", "riya@email.com", 16)
adult = User("Neha", "neha@email.com", 20)
print(f"Age 16 — Adult: {teen.is_adult}")
print(f"Age 20 — Adult: {adult.is_adult}")