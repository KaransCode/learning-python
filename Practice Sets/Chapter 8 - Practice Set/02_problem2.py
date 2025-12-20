# Program to convert Celsius to fahrenheit 

def Celsius_to_fahrenheit(cel):
    Fahrenheit = (cel * 9/5) + 32 
    return Fahrenheit

deg = float(input("Enter Degree in Celsius: "))
print(f"Temperature in Fahrenheit is {Celsius_to_fahrenheit(deg)}")
