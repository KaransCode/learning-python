#  Walrus Operator  Assignment Expression

List = [3,90,21]

if (n := len(List)) > 3 :
    print(f"List is too long. ({n} elements, expected <=3 ) ")
else:
    print(List)