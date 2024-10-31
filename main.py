num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
number = 0
while number <= num2:

    if num1 < num2:
        number = num1 + 1
        total_sum = 0
        while number < num2:
            total_sum += number
            number += 1
        print(f"The sum of numbers between {num1} and {num2} is {total_sum}")
        break
    else:
        print("The first number should be less than the second number.")
        break