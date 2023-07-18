bounceHeight = float(input("Enter the height: "))
bounceQty = int(input("Enter the quantity of bounces: "))

totalDistance = 0
currentHeight = bounceHeight

for i in range(bounceQty):
    totalDistance += currentHeight
    currentHeight *= 0.6
    totalDistance += currentHeight

print("The total distance traveled is: ", totalDistance, "feet.")
