# Variable Naming Rules in Python
# This script explains the rules and conventions for naming variables in Python.


# 1. Start with a letter or underscore
name = "Alice"
_age = 25
# 1name = "Invalid"  # Invalid: starts with a number

# 2. Use only letters, numbers, and underscores
user1 = "Bob"
user_name = "Charlie"
# user-name = "Invalid"  # Invalid: contains a hyphen

# 3. Case-sensitive
x = 1
X = 2
print(x)  # 1
print(X)  # 2

# 4. Don't use Python keywords
# for = 5  # Invalid: 'for' is a keyword

# Naming Conventions
first_name = "Guido"      # snake_case for variables
PI = 3.14                 # ALL_CAPS for constants

class MyClass:            # PascalCase for classes
    pass