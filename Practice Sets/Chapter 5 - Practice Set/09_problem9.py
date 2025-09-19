# Can we change the value 
# inside a list which is contained in set 



# s = {8,7,12,"Karan",[1,2]}
# we cannot add list in a set
# Gives TypeError: unhashable type: 'list'


s1 = {8,12.13,"Karan",True, (1,2,3)}
print(s1) # tuples can be added in a set