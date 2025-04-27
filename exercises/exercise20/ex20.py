fruits = []

while True:
    fruit = input("Enter a fruit: ").lower()

    if fruit == 'done':
        break

    fruits.append(fruit)

print(f"Fruits list: {fruits}")
print(f"There are {len(fruits)} fruits in that list.")