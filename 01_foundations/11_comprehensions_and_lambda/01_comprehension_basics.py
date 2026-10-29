squares=[n**2  for n in range(1,51)]
print("Squares: ",squares)

evens =[n for n in range(1,51) if n%2==0]
print("Evens:", evens)

def is_prime(n):
    if n<2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True    

prime_tag=[
    (n,"prime" if is_prime(n) else "Not prime")
    for n in range(1,51)
]
print("Prime Tag:",prime_tag)

"""Comprehension Basics
Turning loops into list comprehensions
Using list comprehensions over the numbers 1 to 50, build:
• a list of their squares
• a list of only the even numbers
• a list of (number, "prime" / "not prime") tuples

Example (showing the first few of each):

Squares: [1, 4, 9, 16, 25, ...]
Evens:   [2, 4, 6, 8, 10, ...]
Prime tags: [(1,'not prime'), (2,'prime'), (3,'prime'), (4,'not prime'), ...]

Try writing each as a single comprehension line, then compare it to the equivalent for-loop version.
"""