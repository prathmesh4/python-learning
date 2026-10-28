age = int(input("Age: "))
student = input("student (yes/no): ").strip().lower()
day = input("Day : ").strip().lower()

base_price = 200
age_discount = 0
student_discount = 0
weekend_surcharge = 0

if age<12 or age >=60:
    age_discount = base_price * 0.50

if student == "yes":
    student_discount = base_price * 0.20
   
discounted_price = base_price - age_discount - student_discount

if day in ("saturday","sunday"):
    weekend_surcharge = base_price * 0.50        

final_price = discounted_price + weekend_surcharge
print("Base price:  Rs", base_price)
print("Student discount:  -Rs",int(student_discount))
print("Weekend surcharge: +Rs",int(weekend_surcharge))
print("Final price:        Rs",int(final_price))

"""Ticket Pricing System
Combining several conditions into one price
Compute a cinema ticket price from three inputs: age, whether the person is a student (yes/no), and the day of the week.

Rules, applied to a base price of Rs 200:
• Age under 12 OR 60+  -> 50% off the base price
• Student               -> an extra 20% off
• Weekend (Saturday/Sunday) -> add a 50% surcharge, applied AFTER the discounts

Print a clear breakdown and the final price.

Example:

Age: 20
Student (yes/no): yes
Day: Saturday

Base price:        Rs 200
Student discount:  -Rs 40
Weekend surcharge: +Rs 80
Final price:       Rs 240
"""