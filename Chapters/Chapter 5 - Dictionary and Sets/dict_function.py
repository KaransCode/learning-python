# dict_function.py

# Dictionary for demonstration
sample_dict = {
    'name': 'Alice',
    'age': 30,
    'city': 'New York'
}

# 1. get() - Safely get a value for a key
print("1. get():", sample_dict.get('name'))  # Alice

# 2. items() - Get all key-value pairs
print("2. items():", list(sample_dict.items()))

# 3. keys() - Get all keys
print("3. keys():", list(sample_dict.keys()))

# 4. values() - Get all values
print("4. values():", list(sample_dict.values()))

# 5. update() - Update dictionary with another dict
sample_dict.update({'age': 31, 'country': 'USA'})
print("5. update():", sample_dict)

# 6. pop() - Remove item by key and return its value
age = sample_dict.pop('age')
print("6. pop():", age, sample_dict)

# 7. setdefault() - Return value if key exists, else set and return default
country = sample_dict.setdefault('country', 'Unknown')
print("7. setdefault():", country, sample_dict)

# 8. popitem() - Remove and return the last inserted key-value pair
last_item = sample_dict.popitem()
print("8. popitem():", last_item, sample_dict)

# 9. fromkeys() - Create a new dict from keys with a default value
keys = ['a', 'b', 'c']
new_dict = dict.fromkeys(keys, 0)
print("9. fromkeys():", new_dict)

# 10. copy() - Shallow copy of dictionary
copied_dict = sample_dict.copy()
print("10. copy():", copied_dict)

# 11. clear() - Remove all items from dictionary
copied_dict.clear()
print("11. clear():", copied_dict)

# 12. del keyword (Not a method, but used frequently)
# Deleting a key
if 'name' in sample_dict:
    del sample_dict['name']
print("12. del keyword:", sample_dict)

# 13. in keyword - Check if key exists
print("13. 'city' in dict:", 'city' in sample_dict)

# 14. dict comprehension - Create dictionary
squares = {x: x*x for x in range(5)}
print("14. dict comprehension:", squares)

# 15. len() - Get number of items
print("15. len():", len(squares))

# 16. any() and all()
print("16. any():", any(squares))  # True if any key is truthy
print("    all():", all(squares))  # False if any key is 0

# 17. isinstance() to check dict type
print("17. isinstance():", isinstance(squares, dict))

# 18. Reversing keys/values (custom use, not built-in method)
reversed_dict = {v: k for k, v in squares.items()}
print("18. reverse dict:", reversed_dict)
