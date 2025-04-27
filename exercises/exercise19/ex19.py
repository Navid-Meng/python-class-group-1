number = int(input("Enter a number: "))

result = 0

for i in range(1, number+1):
    result += i

print(f"The sum of the numbers from 1 to {number} is {result}")