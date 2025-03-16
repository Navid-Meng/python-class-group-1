first_number = input("Enter the first number: ")
second_number = input("Enter the second number: ")

print("Before swapping: ")
print(f"First number = {first_number}")
print(f"Second number = {second_number}")

first_number, second_number = second_number, first_number

print("\nAfter swapping: ")
print(f"First number = {first_number}")
print(f"Secondd number = {second_number}")