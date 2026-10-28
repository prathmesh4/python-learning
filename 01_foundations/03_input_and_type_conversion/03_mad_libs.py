name = input("Enter a name: ")
animal = input("Enter an Animal: ")
number = int(input("Enter a number: "))
food = input("enter a food: ")
city = input("Enter a city: ")

print(f"\nOne day in {city}, {name} met a talking {animal}")
print(f"The {animal} ate {number} {food}s....  then asked for {number} * 2 = {number *2 } more!")

"""
Mad Libs Story Generator

f-strings, and using a number as both text and math
Ask the user for 5 inputs: a name, an animal, a number, a food, and a city. Then weave them into a funny paragraph using an f-string.

The number must be used TWICE: once as plain text in the story, and once inside a calculation that also appears in the story.

Example:

Enter a name: Aisha
Enter an animal: panda
Enter a number: 3
Enter a food: samosa
Enter a city: Delhi

One day in Delhi, Aisha met a talking panda.
The panda ate 3 samosas... then asked for 3 * 2 = 6 more!
"""