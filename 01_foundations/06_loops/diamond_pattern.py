n = int(input("Enter an odd number: "))

for i in range(1, n + 1, 2):
    spaces = (n - i) // 2
    stars = i
    print(" " * spaces + "*" * stars)
for j in range(n - 2, 0, -2):
    spaces = (n - j) // 2
    stars = j
    print(" " * spaces + "*" * stars)