'''
    Practice Exercises
    Chapter 1: Python Fundamentals
    Lesson 2: Variables and Data Types
'''

# Task 1: Create three variables and print them
first_name = "John"
age = 30
height = 1.75
print("First name:", first_name)
print("Age:", age)
print("Height:", height)

# Task 2: Assign favorite number and convert to string
fav_number = 42
print("My favorite number is: " + str(fav_number))

# Task 3: Temperature variable with message
temp = 23.5
print(f"Today's temperature is: {temp}")

# Task 4: Boolean variable and update
is_raining = True
print("It is raining:", is_raining)
is_raining = False
print("It is raining:", is_raining)

# Task 5: Check data types with type()
x = 15
y = 3.14
z = "Python"
print("Type of x:", type(x))
print("Type of y:", type(y))
print("Type of z:", type(z))

# Task 6: Convert float to integer
price = 19.99
converted_price = int(price)
print("Original:", price)
print("Converted:", converted_price)

# Task 7: String concatenation with variables
name = "Alex"
score = 85
active = True
print(name + " has a score of " + str(score) + " and active status is " + str(active))

# Task 8: None variable and type check
data = None
print("Data value:", data)
print("Data type:", type(data))