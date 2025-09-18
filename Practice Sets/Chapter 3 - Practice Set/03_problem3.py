# Program to detect double spaces in a string 

ex_str = "This is an  example   of String   with double spaces"

find_spaces = ex_str.find("  ")
count_spaces = ex_str.count("  ")

print(find_spaces)
print(count_spaces)