a=10
b=20
c=30

temp=a
a=b
b=c
c=temp

print (a,b,c)

"""The Variable Rotation Puzzle
Reassignment order and why sequence matters
You are given three variables:

a = 10
b = 20
c = 30

Rotate their values so that:
• a takes b's value
• b takes c's value
• c takes a's ORIGINAL value

After the rotation, printing a, b, c should give:

20 30 10

Rules:
• Do it in as few lines as possible.
• Do NOT hardcode 10, 20, or 30 after the initial setup.

In a comment, explain why the ORDER of your assignments matters — what would happen to a's original value if you overwrote it first?"""