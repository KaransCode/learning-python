# -----------------------------
# 👋 Introduction to Functions
# -----------------------------

# A function is a reusable block of code that performs a specific task.
# It helps in organizing code, avoiding repetition, and improving readability.

# ✅ 1. Function Definition
def greet():
    print("Hello! Welcome to the world of functions.")

# ✅ 2. Function with Parameters
def add(a, b):
    result = a + b
    return result

# ✅ 3. Function with Default Parameters
def introduce(name="Guest"):
    print(f"My name is {name}.")

# ✅ 4. Function Returning Multiple Values
def operations(x, y):
    return x + y, x - y, x * y, x / y

# ✅ 5. Calling Functions
greet()  # Calling without parameters

sum_result = add(5, 3)
print("Sum:", sum_result)

introduce("Alice")
introduce()  # Uses default argument

add_result, sub_result, mul_result, div_result = operations(10, 2)
print("Addition:", add_result)
print("Subtraction:", sub_result)
print("Multiplication:", mul_result)
print("Division:", div_result)

# ✅ 6. Function with Conditional Logic
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

print("Is 4 even?", is_even(4))
print("Is 7 even?", is_even(7))
