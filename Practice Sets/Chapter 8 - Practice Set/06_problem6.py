# Program to convert Inches to Centimeters. 

def inch_to_cms(inch):
    centimeter = (inch * 2.54) 
    return centimeter

i = float(input("Enter Measurement in Inches : "))
print(f"Measurement in centimeter is {inch_to_cms(i)}")
