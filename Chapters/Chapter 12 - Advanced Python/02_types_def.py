# Explicit Type Defination 

a = 5 # without type defination

a : int = 101
print(a)
name : str = "karan singh"
dec : float = 12.10
isNew : bool = True

# Explicit Type Defination for function

def sum(a : int, b : int) -> int:
    return a + b

print(sum("Karan","Singh"))
print(sum(10,12))
