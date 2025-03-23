# 1. Print the second color

colors = ["Red", "Green", "Blue", "Yellow"]
print(colors[1])

# 2. Modify Cat to Tiger
animals = ["Dog", "Cat", "Elephant"]
animals[1] = "Tiger"
print(animals)

# 3. List slicing
sequence = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
slice1 = sequence[3:7]
slice2 = sequence[0::3]
print(slice1)
print(slice2)

# 4. Nested list operations
grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(grid[2][1])
grid[1][1] = 50
print(grid)

# 5. Add and remove items
numbers = [10, 20, 30]
numbers.append(40)
numbers.remove(20)
print(numbers)

# 6. Sort 5 numbers in descending order
numbers = [5, 2, 8, 1, 9]
numbers.sort(reverse=True)
print(numbers)

# 7. Sort ages in ascending order
ages = [25, 19, 30, 22, 18]
ages.sort()
print(ages)

# 8. Combine two lists
'''
This exercise can be in two ways: 
first -> use concatenation method
second -> use extend()
'''
list1 = ["A", "B", "C"]
list2 = [1, 2, 3]
print(f"First way: {list1 + list2}")
combined = list1.extend(list2)
print(f"Second way: {list1}")