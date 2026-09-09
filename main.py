# A Python program that explores NOT, XOR, left shift, and right shift operations, showing how bits can be flipped, compared, 
# doubled, or divided using bitwise operators.

num1 = int(input("Enter the 1st number: "))
num2 = int(input("Enter the 2nd number: "))

print("NOT")
print(~num1)
print(~num2)
print()

print("XOR")
print(num1^num2)
print()

print("Left Shift")
print(num1>>1)
print(num2>>1)
print()

print("Right Shift")
print(num1<<1)
print(num2<<1)