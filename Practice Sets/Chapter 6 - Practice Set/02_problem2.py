''' Program to take input of marks of 3 subjects of 1 student And
  Check that atleast 33% is in each subject 
  and to pass total should be 40% either fail '''

name = input("Enter Your Name: ")
eng = int(input(" Enter marks in English: "))
math = int(input(" Enter marks in Maths: "))
sci = int(input(" Enter marks in Science: "))

total = eng + math + sci

if(eng>=33 and math>=33 and sci>=33):
    if((total/3)>= 40):
        print(f"{name}, you passed with {total} marks out of 300!")
        print(f"{name} got {total/3}%!")
    else:
        print(f"{name} got only {total} marks!")
        print(f"You are Failed with only {total/3}%")
else:
    print("You are Failed")

print("End of Program")