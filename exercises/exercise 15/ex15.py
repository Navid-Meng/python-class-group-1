weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

bmi = weight / (height ** 2)

if bmi >= 30:
    category = "obesity"
elif bmi >= 25:
    category = "overweight"
elif bmi >= 18.5:
    category = "normal weight"
else:
    category = "underweight"
    
print(f"Your BMI is {bmi:.2f}.")
print(f"You are in the {category} category.")
