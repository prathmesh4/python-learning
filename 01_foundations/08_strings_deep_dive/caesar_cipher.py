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