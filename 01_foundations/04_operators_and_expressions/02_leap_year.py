year=int(input("Enter a year: "))

divisible_by_4 = year % 4 == 0
divisible_by_100 = year % 100 == 0
divisible_by_400 = year % 400 == 0

is_leap_year = divisible_by_4 and (not divisible_by_100 or divisible_by_400)

print("Divisible by 4: ", divisible_by_4)
print("Divisible by 100: ", divisible_by_100)
print("Divisible by 400: ", divisible_by_400)
print("Is leap year : ", is_leap_year)

"""Leap Year Logic
Boolean logic with operators only — no if/else
A year is a leap year if:
• it is divisible by 4, AND
• it is NOT divisible by 100, UNLESS it is also divisible by 400.

Take a year from the user. WITHOUT using if/else, print each individual condition's boolean result, then the final combined answer built purely from boolean operators (and / or / not).

Example (year = 2000):

Divisible by 4:   True
Divisible by 100: True
Divisible by 400: True
Is leap year:     True

Example (year = 1900):

Divisible by 4:   True
Divisible by 100: True
Divisible by 400: False
Is leap year:     False
"""