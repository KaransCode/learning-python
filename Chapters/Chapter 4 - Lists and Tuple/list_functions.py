# lists_functions.py

print("--- Common List Functions (Methods) and Built-in Functions for Lists ---")
print("-" * 60)

# A sample list to demonstrate various methods
my_list = [10, 20, 30, 40, 20, 50]
print(f"Initial list: {my_list}")
print("-" * 60)

# --- 1. Modification/Manipulation Methods (High Priority) ---

# 1.1. append(item) - Adds an item to the end of the list
my_list.append(60)
print(f"After append(60): {my_list}")
print("-" * 60)

# 1.2. insert(index, item) - Inserts an item at a specified position
my_list.insert(1, 15)
print(f"After insert(1, 15): {my_list}")
print("-" * 60)

# 1.3. extend(iterable) - Appends elements from an iterable to the end of the list
another_list = [70, 80]
my_list.extend(another_list)
print(f"After extend([70, 80]): {my_list}")
print("-" * 60)

# 1.4. remove(value) - Removes the first occurrence of a specified value
my_list.remove(20) # Removes the first 20
print(f"After remove(20): {my_list}")
# my_list.remove(99) # Uncomment to see ValueError if item not found
print("-" * 60)

# 1.5. pop(index) - Removes and returns the item at a given index (last if no index)
popped_item = my_list.pop(0) # Removes item at index 0
print(f"After pop(0): {my_list}, Popped item: {popped_item}")
last_popped = my_list.pop() # Removes last item
print(f"After pop(): {my_list}, Last popped item: {last_popped}")
print("-" * 60)

# 1.6. sort(reverse=False) - Sorts the list in ascending order (in-place)
sort_list = [5, 1, 4, 2, 8]
print(f"List before sort(): {sort_list}")
sort_list.sort()
print(f"After sort(): {sort_list}")
sort_list.sort(reverse=True) # Sort in descending order
print(f"After sort(reverse=True): {sort_list}")
print("-" * 60)

# 1.7. reverse() - Reverses the order of elements in the list (in-place)
reverse_list = [1, 2, 3, 4, 5]
print(f"List before reverse(): {reverse_list}")
reverse_list.reverse()
print(f"After reverse(): {reverse_list}")
print("-" * 60)

# 1.8. clear() - Removes all items from the list
clear_list = [1, 2, 3]
print(f"List before clear(): {clear_list}")
clear_list.clear()
print(f"After clear(): {clear_list}")
print("-" * 60)

# --- 2. Information/Query Methods (Medium Priority) ---

# 2.1. count(value) - Returns the number of times a specified value occurs
count_example = [1, 2, 2, 3, 2, 4]
print(f"List for count(): {count_example}")
print(f"Count of 2: {count_example.count(2)}")
print(f"Count of 5: {count_example.count(5)}")
print("-" * 60)

# 2.2. index(value) - Returns the lowest index of the specified value
# Raises ValueError if the value is not present.
index_example = ['a', 'b', 'c', 'b']
print(f"List for index(): {index_example}")
print(f"Index of 'c': {index_example.index('c')}")
print(f"Index of first 'b': {index_example.index('b')}")
try:
    index_example.index('z')
except ValueError as e:
    print(f"Error using index('z'): {e}")
print("-" * 60)

# --- 3. Built-in Functions (Applied to Lists) ---

# 3.1. len(list) - Returns the number of items in the list
len_list = [10, 20, 30, 40]
print(f"List for len(): {len_list}")
print(f"Length of list: {len(len_list)}")
print("-" * 60)

# 3.2. min(list) - Returns the item with the lowest value
min_list = [5, 1, 9, 2]
print(f"List for min(): {min_list}")
print(f"Minimum value: {min(min_list)}")
print("-" * 60)

# 3.3. max(list) - Returns the item with the highest value
max_list = [5, 1, 9, 2]
print(f"List for max(): {max_list}")
print(f"Maximum value: {max(max_list)}")
print("-" * 60)

# 3.4. sum(list) - Returns the sum of all items in a list of numbers
sum_list = [1, 2, 3, 4, 5]
print(f"List for sum(): {sum_list}")
print(f"Sum of elements: {sum(sum_list)}")
print("-" * 60)

# 3.5. sorted(iterable) - Returns a new sorted list from the items of iterable
# This does not modify the original list.
original_unsorted = [7, 3, 9, 1, 5]
print(f"Original list for sorted(): {original_unsorted}")
new_sorted_list = sorted(original_unsorted)
print(f"New sorted list: {new_sorted_list}")
print(f"Original list remains unchanged: {original_unsorted}")
print("-" * 60)

print("--- End of List Functions ---")
