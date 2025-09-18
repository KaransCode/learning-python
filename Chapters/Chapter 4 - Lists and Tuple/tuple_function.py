# tuple_functions.py

# Sample tuple
numbers = (10, 20, 30, 20, 40, 50, 20)

# len() - length of tuple
print("Length:", len(numbers))

# count() - count occurrences
print("Count of 20:", numbers.count(20))

# index() - first index of value
print("Index of 30:", numbers.index(30))

# min() - smallest value
print("Min:", min(numbers))

# max() - largest value
print("Max:", max(numbers))

# sum() - total of elements
print("Sum:", sum(numbers))

# sorted() - returns sorted list
print("Sorted:", sorted(numbers))

# all() - checks if all are true
print("All true:", all((1, True, 5)))

# any() - checks if any is true
print("Any true:", any((0, False, 5)))

# tuple() - create tuple from iterable
list1 = [1, 2, 3]
new_tuple = tuple(list1)
print("Converted tuple:", new_tuple)
