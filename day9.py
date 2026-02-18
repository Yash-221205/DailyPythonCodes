def tri_area(base, height):
    return 0.5 * base * height

base = float(input("Enter base of triangle: "))
height = float(input("Enter height of triangle: "))

area = tri_area(base, height)

print("Area of triangle:", area)
