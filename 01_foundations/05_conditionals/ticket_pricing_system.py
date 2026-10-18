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