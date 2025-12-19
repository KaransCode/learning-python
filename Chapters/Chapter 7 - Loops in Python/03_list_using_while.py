# 03_list_using_while.py
"""
Using while loop to populate a list
Use case: User input collector
"""
user_inputs = []
count = 0
while count < 3:
    user_inputs.append(input(f"Enter input {count+1}: "))
    count += 1

print("Collected inputs:", user_inputs)