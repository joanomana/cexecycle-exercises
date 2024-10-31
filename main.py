import math
num1=int(input("Enter a number: "))
number = 0
while number <= num1:
    result = math.pow(2,number)
    print(round(result))
    number +=1