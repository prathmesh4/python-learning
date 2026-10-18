a=int(input("enter first non-negative number (a): "))
b=int(input("enter second non-negative number (b): "))

print(f"\na = {a} -> {bin(a)}")
print(f"b = {b} -> {bin(b)}")

and_result= a & b
print(f"a & b = {and_result} ({bin(and_result)})")
or_result= a | b
print(f"a | b = {or_result} ({bin(or_result)})")
xor_result = a ^ b
print(f"a ^ b = {xor_result} ({bin(xor_result)})")
left_shift = a << 1
print(f"a << b = {left_shift} ({bin(left_shift)})")
right_shift = a >> 1
print(f"a >> b = {right_shift} ({bin(right_shift)})")