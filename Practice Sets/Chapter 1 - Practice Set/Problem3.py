# Using external module for performing a task 
# Ensure you have the module installed. You can install it using pip:
# pip install pyjokes


import pyjokes as pj

joke = pj.get_joke();

print(joke)
