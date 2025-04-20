# 1. Squares of even numbers from 0 to 20

squares = [x**2 for x in range(21) if x % 2 == 0]
print("Squares of even numbers from 0 to 20:", squares)

# 2. Words longer than 3 characters

words = ['hi', 'hello', 'sun', 'cat', 'fantastic']
long_words = [word for word in words if len(word) > 3]
print("Words longer than 3 characters:", long_words)

# 3. Dictionary with numbers and their cubes

cubes = {x: x**3 for x in range(1, 5)}
print("Dictionary with numbers and their cubes:", cubes)

# 4. Unique lengths of words

words = ['apple', 'bat', 'cat', 'apple', 'dog']
unique_lengths = {len(word) for word in words}
print("Unique lengths of words:", unique_lengths)