# Program to replace double spaces 
# with single spaces in a string 

ex_str = "This is an example of String  with  double  spaces"

print(ex_str)
find_spaces = ex_str.find("  ")
count_spaces = ex_str.count("  ")

print(find_spaces)
print(count_spaces)

replace_space = ex_str.replace("  "," ")
print(replace_space)
count_spaces = replace_space.count("  ")

print(find_spaces)
print(count_spaces)
