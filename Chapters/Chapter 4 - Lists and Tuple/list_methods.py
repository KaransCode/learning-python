# list_methods.py

# Sample list
items = [3, 1, 4, 1, 5]

# append() - add to end
items.append(9)
print("append:", items)

# insert() - add at index
items.insert(2, 2)
print("insert:", items)

# remove() - remove by value
items.remove(1)
print("remove:", items)

# pop() - remove by index (default last)
items.pop()
print("pop:", items)

# sort() - sort in-place
items.sort()
print("sort:", items)

# reverse() - reverse order
items.reverse()
print("reverse:", items)

# index() - first index of value
print("index of 4:", items.index(4))

# count() - number of occurrences
print("count of 1:", items.count(1))

# extend() - add multiple elements
items.extend([6, 7])
print("extend:", items)

# copy() - shallow copy
copy_items = items.copy()
print("copy:", copy_items)

# clear() - remove all elements
items.clear()
print("clear:", items)
