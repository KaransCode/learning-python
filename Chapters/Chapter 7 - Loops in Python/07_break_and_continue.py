# 07_break_and_continue.py

"""
Demonstrate break and continue statements
Use case: Skipping or stopping iterations
"""
for i in range(1, 6):
    if i == 3:
        continue  # Skip the iteration
    if i == 5:
        break     # Exit the loop
    print("Value:", i)