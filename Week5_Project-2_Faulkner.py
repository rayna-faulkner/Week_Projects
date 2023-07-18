side_a = float(input("Enter the length of side A: "))
side_b = float(input("Enter the length of side B: "))
side_c = float(input("Enter the length of side C: "))

def right_triangle(side_a, side_b, side_c):
    if side_a ** side_b == side_c:
        return True
    else:
        return False

if right_triangle(side_a, side_b, side_c):
    print("This is a right triangle.")
else:
    print("This is not a right triangle.")
