#Given the length and breadth of a rectangle, print area of the rectangle.

def area(l, b):
    area = l * b
    return area
l = float(input("Enter the length of the rectangle: "))
b = float(input("Enter the breadth of the rectangle: "))
area = area(l, b)
print("The area of the rectangle is:", area)