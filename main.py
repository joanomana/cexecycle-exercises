number = int(input("Enter a number: "))
def divider(number):
    dividers = []
    for i in range(1,number+1):
        if number % i ==0:
            dividers.append(i)
    return dividers
dividers = divider(number)
print(f"The dividers of {number} are {' '.join(map(str, dividers))}")