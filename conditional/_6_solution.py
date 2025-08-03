distance  = int(input("Enter the distance to be covered : "))

if distance < 3:
    mode = "Walk"
elif distance <=15:
    mode = "Bike"
else:
    mode = "Car"

print(mode)