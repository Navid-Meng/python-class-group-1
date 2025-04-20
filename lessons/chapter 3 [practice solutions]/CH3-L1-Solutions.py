# 1. Even or Odd

number = 4

if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")
    
# 2. Check if Number is Positive, Negative, or Zero

number = input("Enter a number: ")

if number < 0:
    state = "negative"
elif number > 0:
    state = "positive"
else:
    state = "zero"
    
print(f"The {number} is {state}")

# 3. Voting Eligibility

age = 20
is_citizen = True
eligibility = ""

if age >= 18 and is_citizen:
    eligibility = "eligible to vote"
else:
    eligibility = "not eligible to vote"

print(f"The person is {eligibility}.")

# 4. Grade Evaluation

grade = int(input("Enter your grade (0-100): "))

if grade >= 90:
    evaluation = "A"
elif grade >= 80:
    evaluation = "B"
elif grade >= 70:
    evaluation = "C"
elif grade >= 60:
    evaluation = "D"
else:
    evaluation = "F"

print(f"Your grade is: {evaluation}")

# 5. Nested conditionals for age and gender

age = int(input("Enter your age: "))
gender = input("Enter your gender (male/female): ").lower()

if gender == 'female' and age < 25:
    print("Eligible for discount.")
elif gender == 'male' and age > 65:
    print("Eligible for discount.")
else:
    print("Not eligible for discount.")
    
# 6. Multiple Conditions for Admission
age = int(input("Enter your age: "))
has_diploma = input("Do you have a high school diploma? (yes/no): ").lower() == 'yes'
passed_test = input("Did you pass the admission test? (yes/no): ").lower() == 'yes'

if age >= 18 and has_diploma and passed_test:
    print("You are qualified for admission.")
else:
    print("You are not qualified for admission.")