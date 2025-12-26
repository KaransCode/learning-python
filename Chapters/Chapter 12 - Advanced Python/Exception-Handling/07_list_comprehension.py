#  List comprehension 

List = []
for i in range(10,20):
    List.append(i)
print(List)

Squared_List = [i*i for i in List]
print("After Squaring each element from the List")
print(Squared_List)