#  To find out sum of first n natural number

n = int(input("Enter n: "))

i = 0
Sum=0
while(i<=n):
    Sum+=i
    i+=1

print(f"Sum of first {n} natural number is {Sum}")