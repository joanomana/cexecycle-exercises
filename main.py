minutes = int(input("Enter the time: "))
total_minutes = 0

while minutes > 0:
    total_minutes += minutes
    minutes = int(input("Enter the time: "))

hours = total_minutes // 60
minutes = total_minutes % 60
print(f"Total travel time: {hours} hours and {minutes} minutes")