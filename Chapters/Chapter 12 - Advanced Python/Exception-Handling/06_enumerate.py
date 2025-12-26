# use of enumerate function 

# without enumerate function 
list1 = [21,1,5,62,98]
index = 0
for item in list1:
    print(f"Item at index {index} is {item}")
    index += 1

# Using enumerate function 
print("\nSame as Above with enumerate function ")
list2 = [21,1,5,62,98]
for index, item in enumerate(list2):
    print(f"Item at index {index} is {item}")