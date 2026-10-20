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