# 1
my_set = {1, 2, 3, 4, 5}
my_set.add(2)
print("1:", my_set)

# 2
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
result = set1.intersection(set2)
print("2:", result)

# 3
sentence = "The cat and the dog"
words = sentence.lower().split()
unique_words = set(words)
print("3:", unique_words)

# 4
set1 = {1, 2}
set2 = {2, 3}
result = set1.union(set2)
print("4:", result)

# 5
set1 = {1, 2, 3}
set2 = {2, 3, 4}
result = set1.intersection(set2)
print("5:", result)

# 6
word = "Hello"
unique_letters = set(word.lower())
count = len(unique_letters)
print("6:", count)

# 7
small_set = {1, 2}
big_set = {1, 2, 3}
result = small_set.issubset(big_set)
print("7:", result)

# 8
my_set = set()
my_set.add(1)
my_set.add(2)
my_set.add(3)
print("8:", my_set)

# 9
my_set = {1, 2, 3, 4}
my_set.remove(3)
print("9:", my_set)

# 10
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
result = set1.difference(set2)
print("10:", result)

# 11
my_set = {1, 2, 3}
my_set.clear()
print("11:", my_set)