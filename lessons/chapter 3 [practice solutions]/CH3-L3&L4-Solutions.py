### Exercises for practice

##### 1. **Sum of Sales**
# Calculate the total of a list of sales amounts.
sales = [25.50, 14.99, 33.25, 9.75]
total = 0
for amount in sales:
    total += amount
print(f"Total: ${total:.2f}")

##### 2. **Even Number Printer**
# Print all even numbers from 1 to 20.
for number in range(1, 21):
    if number % 2 == 0:
        print(number, end=" ")
print()

##### 3. **Password Retry Limit**
# Ask the user for a password until they enter "secret" or reach 3 attempts.
attempts = 0
while attempts < 3:
    password = input("Enter password: ")
    if password == "secret":
        print("Access granted!")
        break
    attempts += 1
else:
    print("Locked out!")


##### 4. **Inventory Cleanup**
# Print only items with more than 0 in stock, stopping if a negative value is found.
stock_quantities = [5, 12, 0, 8, -1, 10]
for quantity in stock_quantities:
    if quantity < 0:
        print("Negative stock detected!")
        break
    if quantity > 0:
        print(f"In stock: {quantity}")

##### 5. **Email Validator**
# Check a list of emails and print "Valid" if they contain "@", otherwise skip them.
emails = ["user@domain.com", "no-at-sign", "test@site.org", "plain"]
for email in emails:
    if "@" not in email:
        continue
    print(f"Valid: {email}")

##### 6. **Countdown Timer**
# Simulate a countdown from 10 to 1, printing each number, then "Liftoff!" at the end.
count = 10
while count > 0:
    print(count, end=" ")
    count -= 1
print("Liftoff!")
