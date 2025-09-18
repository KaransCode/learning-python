# intro_tuple.py

# Tuple creation
fruits = ("apple", "banana", "cherry")

print(fruits)

# Accessing elements
print("First fruit:", fruits[0])

# Length of tuple
print("Number of fruits:", len(fruits))

# Tuple with mixed data types
person = ("Alice", 30, "Engineer")
print("Person info:", person)

# Tuple unpacking
name, age, job = person
print("Name:", name)
print("Age:", age)
print("Job:", job)

# Tuples are immutable
try:
    fruits[1] = "orange"
except TypeError as e:
    print("Error:", e)

# Tuple with one element
single_item = ("apple",)
print("Single item tuple:", single_item)

# Loop through tuple
for fruit in fruits:
    print("Fruit:", fruit)
