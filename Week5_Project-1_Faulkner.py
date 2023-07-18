def equilateral_triangle(side_a,side_b,side_c):
    if side_a == side_b == side_c:
        return True
    else:
        return False

side_a = float(input("Please enter the length of side A: "))
side_b = float(input("Please enter the length of side B: "))
side_c= float(input("Please enter the length of side C: "))

if equilateral_triangle(side_a,side_b,side_c):
    print("This triangle is equilateral")
else:
    print ("This triangle is not equilateral")
    
