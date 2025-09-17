# type_casting.py

# The type() function is used to determine the type of an object.
print("--- Using type() function ---")
integer_var = 10
float_var = 10.5
string_var = "Hello"
list_var = [1, 2, 3]
tuple_var = (4, 5)
dict_var = {"a": 1, "b": 2}
set_var = {7, 8, 9}
boolean_var = True

print(f"Value of integer_var: {integer_var}")
print(f"Type of {integer_var}: {type(integer_var)}")
print(f"Value of float_var: {float_var}")
print(f"Type of {float_var}: {type(float_var)}")
print(f"Value of string_var: '{string_var}'")
print(f"Type of '{string_var}': {type(string_var)}")
print(f"Value of list_var: {list_var}")
print(f"Type of {list_var}: {type(list_var)}")
print(f"Value of tuple_var: {tuple_var}")
print(f"Type of {tuple_var}: {type(tuple_var)}")
print(f"Value of dict_var: {dict_var}")
print(f"Type of {dict_var}: {type(dict_var)}")
print(f"Value of set_var: {set_var}")
print(f"Type of {set_var}: {type(set_var)}")
print(f"Value of boolean_var: {boolean_var}")
print(f"Type of {boolean_var}: {type(boolean_var)}")
print("\n")

# Type Casting Functions
# These functions convert one data type to another.

print("--- Type Casting Functions ---")

# 1. int() - Converts to integer
str_num = "123"
float_num = 45.67
bool_val = True
print(f"Value of str_num: '{str_num}'")
print(f"int('{str_num}'): {int(str_num)}")
print(f"Value of float_num: {float_num}")
print(f"int({float_num}): {int(float_num)}") # Truncates decimal part
print(f"Value of bool_val: {bool_val}")
print(f"int({bool_val}): {int(bool_val)}")
print("\n")

# 2. float() - Converts to floating-point number
int_num = 100
str_float = "98.76"
print(f"Value of int_num: {int_num}")
print(f"float({int_num}): {float(int_num)}")
print(f"Value of str_float: '{str_float}'")
print(f"float('{str_float}'): {float(str_float)}")
print("\n")

# 3. str() - Converts to string
int_val = 500
float_val = 123.45
list_val = [10, 20]
print(f"Value of int_val: {int_val}")
print(f"str({int_val}): '{str(int_val)}'")
print(f"Value of float_val: {float_val}")
print(f"str({float_val}): '{str(float_val)}'")
print(f"Value of list_val: {list_val}")
print(f"str({list_val}): '{str(list_val)}'")
print("\n")

# 4. list() - Converts to list
string_to_list = "Python"
tuple_to_list = (1, 2, 3)
set_to_list = {4, 5, 6}
print(f"Value of string_to_list: '{string_to_list}'")
print(f"list('{string_to_list}'): {list(string_to_list)}")
print(f"Value of tuple_to_list: {tuple_to_list}")
print(f"list({tuple_to_list}): {list(tuple_to_list)}")
print(f"Value of set_to_list: {set_to_list}")
print(f"list({set_to_list}): {list(set_to_list)}")
print("\n")

# 5. tuple() - Converts to tuple
string_to_tuple = "Hello"
list_to_tuple = [10, 20, 30]
set_to_tuple = {7, 8, 9}
print(f"Value of string_to_tuple: '{string_to_tuple}'")
print(f"tuple('{string_to_tuple}'): {tuple(string_to_tuple)}")
print(f"Value of list_to_tuple: {list_to_tuple}")
print(f"tuple({list_to_tuple}): {tuple(list_to_tuple)}")
print(f"Value of set_to_tuple: {set_to_tuple}")
print(f"tuple({set_to_tuple}): {tuple(set_to_tuple)}")
print("\n")

# 6. dict() - Converts to dictionary
# Requires a sequence of key-value pairs (e.g., list of tuples)
list_of_tuples = [('name', 'Alice'), ('age', 30)]
print(f"Value of list_of_tuples: {list_of_tuples}")
print(f"dict({list_of_tuples}): {dict(list_of_tuples)}")
print("\n")

# 7. set() - Converts to set (removes duplicates and orders)
list_to_set = [1, 2, 2, 3, 4, 4]
string_to_set = "programming"
print(f"Value of list_to_set: {list_to_set}")
print(f"set({list_to_set}): {set(list_to_set)}")
print(f"Value of string_to_set: '{string_to_set}'")
print(f"set('{string_to_set}'): {set(string_to_set)}")
print("\n")

# 8. bool() - Converts to boolean
# Empty sequences, 0, and None are False; everything else is True
print(f"bool(0): {bool(0)}")
print(f"bool(1): {bool(1)}")
print(f"bool(''): {bool('')}")
print(f"bool('hello'): {bool('hello')}")
print(f"bool([]): {bool([])}")
print(f"bool([1, 2]): {bool([1, 2])}")
print(f"bool(None): {bool(None)}")
print("\n")
