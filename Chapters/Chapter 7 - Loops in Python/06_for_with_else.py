# 06_for_with_else.py

"""
Using for-else to detect if a loop was broken
Use case: Search in list with confirmation
"""
nums = [2, 4, 6, 8, 10]
target = 5
for num in nums:
    if num == target:
        print("Found target!")
        break
else:
    print("Target not found.")