# intro_to_strings.py

print("--- Introduction to Strings in Python ---")

# 1. Defining Strings
# Strings can be defined using single, double, or triple quotes.
single_quote_str = 'Hello, Python!'
double_quote_str = "Learning Strings"
triple_quote_str = """This is a multi-line string.
It can span across several lines."""

print(f"Single quoted: {single_quote_str}")
print(f"Double quoted: {double_quote_str}")
print(f"Triple quoted:\n{triple_quote_str}")
print("\n")

# 2. Accessing Characters (Indexing)
# Strings are sequences, characters can be accessed by their index.
# Index starts from 0 for the first character.
my_string = "Python"
print(f"Original string: {my_string}")
print(f"First character (index 0): {my_string[0]}")
print(f"Third character (index 2): {my_string[2]}")
# Negative indexing accesses from the end (-1 is the last character)
print(f"Last character (index -1): {my_string[-1]}")
print("\n")

# 3. Slicing Strings
# Extract a portion (substring) of a string.
# Syntax: [start:end:step]
print(f"String for slicing: {my_string}")
print(f"Characters from index 2 to 4 (exclusive): {my_string[2:5]}")
print(f"Characters from beginning to index 3 (exclusive): {my_string[:3]}")
print(f"Characters from index 1 to end: {my_string[1:]}")
print(f"Copy of the string: {my_string[:]}")
print(f"Every second character: {my_string[::2]}")
print(f"Reversed string: {my_string[::-1]}")
print("\n")

# 4. String Concatenation (Joining Strings)
# Use the + operator to combine strings.
greeting = "Hello"
name = "Alice"
full_message = greeting + ", " + name + "!"
print(f"Concatenated string: {full_message}")
print("\n")

# 5. String Repetition
# Use the * operator to repeat a string.
repeated_string = "Ha" * 3
print(f"Repeated string: {repeated_string}")
print("\n")

# 6. String Length
# Use the len() function to get the number of characters.
text = "Programming"
print(f"Length of '{text}': {len(text)}")
print("\n")

# 7. String Immutability
# Strings cannot be changed after they are created.
# Any operation that seems to modify a string actually creates a new one.
# For example, my_string[0] = 'J' would cause an error.
immutable_example = "immutable"
new_string = immutable_example.upper() # Creates a new string
print(f"Original: {immutable_example}, New (upper): {new_string}")
print("\n")

# 8. Common String Methods
# Strings have many built-in methods for manipulation.
sample_str = "   Python Programming is FUN!   "
print(f"Original for methods: '{sample_str}'")

# Convert to uppercase
print(f"Uppercase: '{sample_str.upper()}'")
# Convert to lowercase
print(f"Lowercase: '{sample_str.lower()}'")
# Remove leading/trailing whitespace
print(f"Stripped: '{sample_str.strip()}'")
# Split string into a list of substrings based on a delimiter
words = sample_str.strip().split(" ")
print(f"Split into words: {words}")
# Replace occurrences of a substring
replaced_str = sample_str.replace("FUN", "GREAT")
print(f"Replaced 'FUN' with 'GREAT': '{replaced_str}'")
# Find the first occurrence of a substring (-1 if not found)
print(f"Index of 'Programming': {sample_str.find('Programming')}")
print(f"Index of 'Java': {sample_str.find('Java')}")
# Check if a string starts or ends with a substring
print(f"Starts with '   Python': {sample_str.startswith('   Python')}")
print(f"Ends with 'FUN!   ': {sample_str.endswith('FUN!   ')}")
print("\n")

print("--- End of String Basics ---")
