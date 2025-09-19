#  Program to create a dictionary of hindi words
#  with values as their english translation

hin_to_eng = {
        "kela" : "Banana",
        "dukhi" : "Sad",
        "khush" : "Happy",
        "pani" : "Water",
        "Madad"  : "Help",
        "Kursi"  : "Chair",
        "Pankha" : "Fan"
}

print(hin_to_eng)
word = input("Enter the word you to search the meaning :")

print(hin_to_eng[word])

