# intro_dictionary.py

# Creating a dictionary
person = {"name": "Karan Singh", "age": 21, "job": "Engineer"}

# Accessing values
print("Name:", person["name"])

# Adding a new key-value pair
person["city"] = "Madhya Pradesh"
print("Updated:", person)

# Updating a value
person["age"] = 25
print("Age updated:", person)

# Removing a key
del person["job"]
print("After deletion:", person)

# Looping through keys and values
for key, value in person.items():
    print(key, ":", value)

# Check if key exists
if "name" in person:
    print("Name exists")

# Dictionary length
print("Total items:", len(person))

d = {"A" : "C", "A" : "C++",
     "B" : "C++","C" : "Java", "D" : "Java",
     "E" : "C++"}
print(d)
print(len(d))