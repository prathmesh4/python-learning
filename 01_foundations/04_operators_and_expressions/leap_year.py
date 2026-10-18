year=int(input("Enter a year: "))

divisible_by_4 = year % 4 == 0
divisible_by_100 = year % 100 == 0
divisible_by_400 = year % 400 == 0

is_leap_year = divisible_by_4 and (not divisible_by_100 or divisible_by_400)

print("Divisible by 4: ", divisible_by_4)
print("Divisible by 100: ", divisible_by_100)
print("Divisible by 400: ", divisible_by_400)
print("Is leap year : ", is_leap_year)