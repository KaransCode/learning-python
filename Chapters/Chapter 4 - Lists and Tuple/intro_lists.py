# intro_lists.py

print("--- Introduction to Lists in Python ---")

# 1. Defining Lists
# Lists are ordered collections of items. They are mutable (changeable).
# Items can be of different data types.
my_list = [1, 2, 3, "apple", "banana", True]
empty_list = []
print(f"My list: {my_list}")
print(f"Empty list: {empty_list}")
print("\n")

# 2. Accessing Elements (Indexing)
# Elements are accessed by their index, starting from 0.
print(f"Original list for indexing: {my_list}")
print(f"First element (index 0): {my_list[0]}")
print(f"Third element (index 2): {my_list[2]}")
# Negative indexing accesses from the end (-1 is the last element)
print(f"Last element (index -1): {my_list[-1]}")
print("\n")

# 3. Slicing Lists
# Extract a portion (sub-list) of a list.
# Syntax: [start:end:step]
print(f"List for slicing: {my_list}")
print(f"Elements from index 1 to 4 (exclusive): {my_list[1:5]}")
print(f"Elements from beginning to index 3 (exclusive): {my_list[:3]}")
print(f"Elements from index 3 to end: {my_list[3:]}")
print(f"Copy of the list: {my_list[:]}")
print(f"Every second element: {my_list[::2]}")
print(f"Reversed list: {my_list[::-1]}")
print("\n")

# 4. List Mutability (Changing Elements)
# Unlike strings, lists can be changed after creation.
mutable_list = ["red", "green", "blue"]
print(f"Original mutable list: {mutable_list}")
mutable_list[1] = "yellow" # Change an element
print(f"After changing index 1: {mutable_list}")
mutable_list[0:2] = ["orange", "purple"] # Change a slice
print(f"After changing slice [0:2]: {mutable_list}")
print("\n")

# 5. List Concatenation (Joining Lists)
# Use the + operator to combine lists.
list1 = [10, 20]
list2 = [30, 40]
combined_list = list1 + list2
print(f"Combined list: {combined_list}")
print("\n")

# 6. List Repetition
# Use the * operator to repeat a list.
repeated_list = [0] * 5
print(f"Repeated list: {repeated_list}")
print("\n")

# 7. List Length
# Use the len() function to get the number of elements.
another_list = ["a", "b", "c", "d"]
print(f"Length of {another_list}: {len(another_list)}")
print("\n")
print(type(another_list))