# operators.py

# 1. Arithmetic Operators
# Used for mathematical operations
print("--- Arithmetic Operators ---")
a = 10
b = 3

print("a = ",a,"\nb = ",b)
print(f"\na + b = {a + b}")   # Addition
print(f"a - b = {a - b}")   # Subtraction
print(f"a * b = {a * b}")   # Multiplication
print(f"a / b = {a / b}")   # Division (float result)
print(f"a % b = {a % b}")   # Modulus (remainder)
print(f"a // b = {a // b}") # Floor Division (integer result)
print(f"a ** b = {a ** b}") # Exponentiation (a to the power of b)
print("\n")

# 2. Comparison (Relational) Operators
# Used to compare two values
print("--- Comparison Operators ---")
x = 5
y = 10
print("x =",x, "\ny = ",y)
print(f"\nx == y: {x == y}") # Equal to
print(f"x != y: {x != y}") # Not equal to
print(f"x > y: {x > y}")   # Greater than
print(f"x < y: {x < y}")   # Less than
print(f"x >= y: {x >= y}") # Greater than or equal to
print(f"x <= y: {x <= y}") # Less than or equal to
print("\n")

# 3. Assignment Operators
# Used to assign values to variables
print("--- Assignment Operators ---")
c = 20
print("c = 20\n")
print(f"Initial c: {c}")
c += 5 # c = c + 5
print(f"c after += 5: {c}")
c -= 3 # c = c - 3
print(f"c after -= 3: {c}")
c *= 2 # c = c * 2
print(f"c after *= 2: {c}")
c /= 4 # c = c / 4
print(f"c after /= 4: {c}")
c %= 3 # c = c % 3
print(f"c after %= 3: {c}")
c //= 1 # c = c // 1
print(f"c after //= 1: {c}")
c **= 2 # c = c ** 2
print(f"c after **= 2: {c}")
print("\n")

# 4. Logical Operators
# Used to combine conditional statements
print("--- Logical Operators ---")
p = True
q = False
print("p = True")
print("q = ",q)

print(f"\np and q: {p and q}") # Logical AND
print(f"p or q: {p or q}")   # Logical OR
print(f"not p: {not p}")     # Logical NOT
print("\n")

# 5. Bitwise Operators
# Used to perform operations on binary digits
print("--- Bitwise Operators ---")
num1 = 10  # Binary: 1010
num2 = 4   # Binary: 0100

print("num1 = 10")
print("num2 = 4\n")
print(f"num1 & num2: {num1 & num2}") # Bitwise AND
print(f"num1 | num2: {num1 | num2}") # Bitwise OR
print(f"num1 ^ num2: {num1 ^ num2}") # Bitwise XOR
print(f"~num1: {~num1}")             # Bitwise NOT (complement)
print(f"num1 << 2: {num1 << 2}")     # Left shift
print(f"num1 >> 2: {num1 >> 2}")     # Right shift
print("\n")

# 6. Identity Operators
# Used to compare the memory locations of two objects
print("--- Identity Operators ---")
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1
print(f"list1 is list2: {list1 is list2}")   # False, different memory locations
print(f"list1 is list3: {list1 is list3}")   # True, same memory location
print(f"list1 is not list2: {list1 is not list2}") # True
print("\n")

# 7. Membership Operators
# Used to test if a sequence contains a value
print("--- Membership Operators ---")
my_string = "Hello Python"
my_list = [10, 20, 30, 40]
print(f"'Python' in my_string: {'Python' in my_string}")   # True
print(f"'Java' in my_string: {'Java' in my_string}")     # False
print(f"20 in my_list: {20 in my_list}")               # True
print(f"50 not in my_list: {50 not in my_list}")         # True
print("\n")
