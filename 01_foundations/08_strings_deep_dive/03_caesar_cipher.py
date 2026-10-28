def caesar_cipher(message, shift):
    result = ""
    for char in message:
        if "a" <= char <= "z":
            shifted = (ord(char) - ord("a") + shift) % 26
            result += chr(shifted + ord("a"))
        elif "A" <= char <= "Z":
            shifted = (ord(char) - ord("A") + shift) % 26
            result += chr(shifted + ord("A"))
        else:
            result += char
    return result

message = input("Enter a message: ")
shift = int(input("Enter shift amount: "))

encoded = caesar_cipher(message, shift)
decoded = caesar_cipher(encoded, -shift)

print("\nOriginal:", message)
print("Encoded: ", encoded)
print("Decoded: ", decoded)
print("Round-trip successful:", decoded == message)

"""Caesar Cipher
Character math and preserving structure
Build an encoder and a decoder for a Caesar cipher with a given shift.

Rules:
• Shift letters by the given amount, wrapping around (z + 1 -> a)
• Preserve case (uppercase stays uppercase, lowercase stays lowercase)
• Leave non-letters (spaces, digits, punctuation) unchanged

Demonstrate a round-trip: encode a message, then decode it back to the original to prove it matches.

Example (shift = 3):

Original: Hello, Tab47!
Encoded:  Khoor, Wde47!
Decoded:  Hello, Tab47!
"""