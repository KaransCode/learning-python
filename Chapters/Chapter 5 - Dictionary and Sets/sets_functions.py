# sets_function.py

# Sample sets for demonstration
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

print("Original sets:")
print("set_a:", set_a)
print("set_b:", set_b)
print()

# 1. add() - Add single element
set_a.add(7)
print("1. add(7):", set_a)

# 2. update() - Add multiple elements from iterable
set_a.update([8, 9])
print("2. update(8,9):", set_a)

# 3. remove() - Remove element, KeyError if not found
set_a.remove(9)
print("3. remove(9):", set_a)

# 4. discard() - Remove element, no error if not found
set_a.discard(10)
print("4. discard():", set_a)

# 5. union() - Return union of sets
union_set = set_a.union(set_b)
print("5. union():", union_set)

# 6. intersection() - Return common elements
intersection_set = set_a.intersection(set_b)
print("6. intersection():", intersection_set)

# 7. difference() - Return elements only in set_a
difference_set = set_a.difference(set_b)
print("7. difference():", difference_set)

# 8. symmetric_difference() - Return elements in either, not both
symmetric_diff = set_a.symmetric_difference(set_b)
print("8. symmetric_difference():", symmetric_diff)

# 9. issubset() - Check if set is subset
print("9. issubset():", {1, 2}.issubset(set_a))  # True

# 10. issuperset() - Check if set is superset
print("10. issuperset():", set_a.issuperset({1, 2}))  # True

# 11. isdisjoint() - Check if sets have no common elements
print("11. isdisjoint():", {10, 11}.isdisjoint(set_a))  # True

# 12. pop() - Remove and return arbitrary item
popped = set_a.pop()
print("12. pop():", popped, set_a)

# 13. clear() - Remove all elements
temp_set = {1, 2, 3}
temp_set.clear()
print("13. clear():", temp_set)

# 14. copy() - Shallow copy of a set
copy_set = set_b.copy()
print("14. copy():", copy_set)

# 15. len() - Get size of set
print("15. len():", len(set_b))

# 16. in keyword - Membership test
print("16. '3 in set_b':", 3 in set_b)

# 17. set() constructor - Convert iterable to set
list_to_set = set([1, 2, 2, 3])
print("17. set() constructor:", list_to_set)

# 18. set comprehension - Create set with conditions
squared_set = {x * x for x in range(5)}
print("18. set comprehension:", squared_set)

# 19. frozenset() - Immutable set
frozen = frozenset([1, 2, 3])
print("19. frozenset():", frozen)
# frozen.add(4)  # Would raise AttributeError