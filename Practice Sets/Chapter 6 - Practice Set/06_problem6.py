#  program to calculate the grade of a student acc. to his marks

st_marks = int(input("Enter your marks: "))

if(st_marks <= 100 and st_marks >= 90):
    print("You got Grade - Excellent ")
elif(st_marks < 90 and st_marks >= 80):
    print("You got Grade - A ")
elif(st_marks < 80 and st_marks >= 70):
    print("You got Grade - B ")
elif(st_marks < 70 and st_marks >= 60):
    print("You got Grade - C ")
elif(st_marks < 60 and st_marks >= 50):
    print("You got Grade - D ")
else:
    print("You got Grade - F ")

