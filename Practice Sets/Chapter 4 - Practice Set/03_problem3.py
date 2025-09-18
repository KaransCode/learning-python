# Checking if a tuple can be changed in python

a_tuple = (10,101,21,1)
print(a_tuple)
print(type(a_tuple))


try:
    a_tuple[3] = 211
except TypeError as e:
    print(e)

print(sorted(a_tuple))

