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

"""
Bitwise Explorer
Binary representation and bitwise operators
Take two small non-negative integers and explore how the computer sees them in binary.

For each number, print its binary form. Then show the result of these bitwise operations, each with its binary breakdown: AND (&), OR (|), XOR (^), left shift (<<), and right shift (>>).

Example (a = 5, b = 3):

a = 5  -> 0b101
b = 3  -> 0b011
a & b  = 1  (0b001)
a | b  = 7  (0b111)
a ^ b  = 6  (0b110)
a << 1 = 10 (0b1010)
a >> 1 = 2  (0b10)

Hint: use bin() to get the binary string of a number.
"""