n = int(input("Enter an odd number: "))

for i in range(1, n + 1, 2):
    spaces = (n - i) // 2
    stars = i
    print(" " * spaces + "*" * stars)
for j in range(n - 2, 0, -2):
    spaces = (n - j) // 2
    stars = j
    print(" " * spaces + "*" * stars)
    
"""Diamond Pattern Generator
Nested loops and spacing math
Ask for an odd number n and print a diamond of stars: n rows in the top half (including the widest middle row), then mirror it for the bottom half.

Example (n = 3):

  *
 ***
*****
 ***
  *

For each row you need to work out how many leading spaces and how many stars to print. Use loops for both halves — don't hardcode the rows.
"""