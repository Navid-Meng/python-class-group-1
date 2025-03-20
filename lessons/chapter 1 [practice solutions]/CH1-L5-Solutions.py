''' 1. Write an expression to calculate the perimeter of a rectangle.'''
length = 2
width = 5

perimeter = 2 * (length + width)

'''2. Check if a number is divisible by both 3 and 5.'''

number = 30  # Example number
is_divisible = (number % 3 == 0) and (number % 5 == 0)
print(is_divisible)  # True if divisible by both, False otherwise

'''
3. Write a program that:
Asks the user to input two numbers.
Prints the results of addition, subtraction, multiplication, division, and modulus operations.
'''

# Get input from user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2 
modulus = num1 % num2

# Print results
print(f"Addition: {addition}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {multiplication}")
print(f"Division: {division}")
print(f"Modulus: {modulus}")

'''
4. Write a program that:
Asks the user to input a base number.
Calculates and prints the result of raising the base to the powers of 1, 2, and 3 using the ** operator.
'''

# Get input from user
base = float(input("Enter a base number: "))

# Calculate powers
power1 = base ** 1
power2 = base ** 2
power3 = base ** 3

# Print results
print(f"{base} to the power of 1 is: {power1}")
print(f"{base} to the power of 2 is: {power2}")
print(f"{base} to the power of 3 is: {power3}")

'''
5. Write a program that:
Asks the user if it's sunny (yes/no) and if it's warm (yes/no).
Converts responses to booleans (True for "yes", False for "no").
Uses and, or, and not operators to print:
Is it sunny AND warm?
Is it sunny OR warm?
Is it NOT sunny?
'''

# Get input from user
sunny_response = input("Is it sunny? (yes/no): ")
warm_response = input("Is it warm? (yes/no): ")

# Convert to boolean
is_sunny = sunny_response == "yes"
is_warm = warm_response == "yes"

# Perform logical operations
sunny_and_warm = is_sunny and is_warm
sunny_or_warm = is_sunny or is_warm
not_sunny = not is_sunny

# Print results
print(f"Is it sunny AND warm? {sunny_and_warm}")
print(f"Is it sunny OR warm? {sunny_or_warm}")
print(f"Is it NOT sunny? {not_sunny}")

'''
6. Create a program that:
Asks the user to input a starting score.
Uses assignment operators (+=, -=, *= ) to:
Add 5 to the score.
Subtract 3 from the score.
Multiply the score by 2.
Prints the score after each operation.
'''

# Get input from user
score = float(input("Enter a starting score: "))

# Perform operations with assignment operators
score += 5
print(f"After adding 5: {score}")

score -= 3
print(f"After subtracting 3: {score}")

score *= 2
print(f"After multiplying by 2: {score}")

'''
9. Create a program that:
Asks the user to input two numbers.
Uses comparison operators (>, <, ==, !=) to check and print whether the first number is greater than, less than, equal to, or not equal to the second.
'''

# Get input from user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform comparisons
greater = num1 > num2
less = num1 < num2
equal = num1 == num2
not_equal = num1 != num2

# Print results
print(f"Is {num1} greater than {num2}? {greater}")
print(f"Is {num1} less than {num2}? {less}")
print(f"Is {num1} equal to {num2}? {equal}")
print(f"Is {num1} not equal to {num2}? {not_equal}")