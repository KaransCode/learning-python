# strings_functions.py

print("--- Common String Functions (Methods) in Python ---")

# A sample string to demonstrate various methods
s = "  Hello Python Programming!   "
print(f"Original string: '{s}'")
print("-" * 40)

# 1. len() - Returns the length of the string
# Note: len() is a built-in function, not a string method.
print(f"Length of string: {len(s)}")
print("-" * 40)

# 2. str.strip() - Removes leading and trailing whitespace
stripped_s = s.strip()
print(f"After strip(): '{stripped_s}'")
print("-" * 40)

# 3. str.lower() - Converts all characters to lowercase
lower_s = s.lower()
print(f"After lower(): '{lower_s}'")
print("-" * 40)

# 4. str.upper() - Converts all characters to uppercase
upper_s = s.upper()
print(f"After upper(): '{upper_s}'")
print("-" * 40)

# 5. str.capitalize() - Converts the first character to uppercase, rest to lowercase
capitalized_s = s.capitalize()
print(f"After capitalize(): '{capitalized_s}'")
print("-" * 40)

# 6. str.title() - Converts the first character of each word to uppercase
title_s = s.title()
print(f"After title(): '{title_s}'")
print("-" * 40)

# 7. str.count(substring) - Returns the number of occurrences of a substring
count_o = s.count('o')
count_py = s.count('P')
print(f"Count of 'o': {count_o}")
print(f"Count of 'P': {count_py}")
print("-" * 40)

# 8. str.find(substring) - Returns the lowest index of the substring (-1 if not found)
find_python = s.find("Python")
find_java = s.find("Java")
print(f"Index of 'Python': {find_python}")
print(f"Index of 'Java': {find_java}")
print("-" * 40)

# 9. str.index(substring) - Same as find(), but raises ValueError if not found
try:
    index_prog = s.index("Programming")
    print(f"Index of 'Programming': {index_prog}")
    # index_error = s.index("C++") # Uncomment to see ValueError
except ValueError as e:
    print(f"Error using index(): {e}")
print("-" * 40)

# 10. str.replace(old, new, count) - Replaces occurrences of a substring
replaced_s = s.replace("Python", "Java")
print(f"After replace('Python', 'Java'): '{replaced_s}'")
replace_limited = s.replace("o", "X", 1) # Replace only the first 'o'
print(f"After replace('o', 'X', 1): '{replace_limited}'")
print("-" * 40)

# 11. str.split(delimiter) - Splits string into a list of substrings
words_space = s.strip().split(" ")
print(f"Split by space: {words_space}")
data = "apple,banana,cherry"
fruits = data.split(",")
print(f"Split by comma: {fruits}")
print("-" * 40)

# 12. str.join(iterable) - Joins elements of an iterable with the string as a separator
my_list = ["Hello", "World", "Python"]
joined_space = " ".join(my_list)
joined_dash = "-".join(my_list)
print(f"Joined with space: '{joined_space}'")
print(f"Joined with dash: '{joined_dash}'")
print("-" * 40)

# 13. str.startswith(prefix) - Checks if string starts with a prefix
print(f"Starts with '  Hello': {s.startswith('  Hello')}")
print(f"Starts with 'Python': {s.startswith('Python')}")
print("-" * 40)

# 14. str.endswith(suffix) - Checks if string ends with a suffix
print(f"Ends with '   ': {s.endswith('   ')}")
print(f"Ends with 'g!': {s.endswith('g!')}")
print("-" * 40)

# 15. str.isalpha() - Checks if all characters are alphabetic
alpha_str = "HelloWorld"
num_str = "123"
print(f"'{alpha_str}'.isalpha(): {alpha_str.isalpha()}")
print(f"'{num_str}'.isalpha(): {num_str.isalpha()}")
print("-" * 40)

# 16. str.isdigit() - Checks if all characters are digits
digit_str = "12345"
mixed_str = "123a"
print(f"'{digit_str}'.isdigit(): {digit_str.isdigit()}")
print(f"'{mixed_str}'.isdigit(): {mixed_str.isdigit()}")
print("-" * 40)

# 17. str.isalnum() - Checks if all characters are alphanumeric (letters or numbers)
alphanum_str = "Python3"
symbol_str = "Py@thon"
print(f"'{alphanum_str}'.isalnum(): {alphanum_str.isalnum()}")
print(f"'{symbol_str}'.isalnum(): {symbol_str.isalnum()}")
print("-" * 40)

# 18. str.isspace() - Checks if all characters are whitespace
space_str = "   \n\t"
non_space_str = " hello "
print(f"'   \\n\\t'.isspace(): {space_str.isspace()}")
print(f"' hello '.isspace(): {non_space_str.isspace()}")
print("-" * 40)

# 19. str.islower() - Checks if all cased characters are lowercase
print(f"'{'hello'.islower()}': {'hello'.islower()}")
print(f"'{'Hello'.islower()}': {'Hello'.islower()}")
print("-" * 40)

# 20. str.isupper() - Checks if all cased characters are uppercase
print(f"'{'HELLO'.isupper()}': {'HELLO'.isupper()}")
print(f"'{'Hello'.isupper()}': {'Hello'.isupper()}")
print("-" * 40)

print("--- End of String Functions ---")
