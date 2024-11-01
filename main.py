print("Draw a rectangle!")
height = int(input("Enter the height: "))
broad = int(input("Enter the broad: "))

rectangle = (height * broad) /3
for i in range(height):
    for j in range(broad):
        print("*", end="")
    print("")



print("")
print("Draw a triangle")
height = int(input("Enter the height: "))

for i in range(height):
    for j in range(i + 1):
        print("*", end="")
    print("")

print("")
print("Draw a hexagon")
size = int(input("Enter the size: "))

# Upper part of the hexagon
for i in range(size):
    print(" " * (size - i - 1) + "*" * (size + 2 * i))

# Lower part of the hexagon
for i in range(size - 1, -1, -1):
    print(" " * (size - i - 1) + "*" * (size + 2 * i))