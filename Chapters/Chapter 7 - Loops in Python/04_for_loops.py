# 04_for_loops.py
"""
Using for loops to iterate over different structures
Use case: Print items in a list and dictionary
"""
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("Fruit:", fruit)

student_scores = {"Alice": 90, "Bob": 82}
for student, score in student_scores.items():
    print(f"{student} scored {score}")