# Merge Dict. & Update operators 

dict1 = { "a" : 1 , "b" : 21 }
dict2 = { "b" : 9 , "d" : 44 }

merged = dict1 | dict2
print(merged)

# Multiple Files Processing 
# with (
#     open('file1.txt') as f1,
#     open('file2.txt') as f2,
#     open('file3.txt') as f3,
#     open('file4.txt') as f4
# ):