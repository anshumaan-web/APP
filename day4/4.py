#Given the length of 3 sides of a triangle, check whether the triangle is valid or not.

def is_valid_triangle(l1, l2, l3):
    l1 = float(l1)
    l2 = float(l2)
    l3 = float(l3)
    if (l1 + l2 > l3) and (l1 + l3 > l2) and (l2 + l3 > l1):
        return True
    else:
        return False
length_1 = input("Enter side 1: ")
length_2 = input("Enter side 2: ")
length_3 = input("Enter side 3: ")
if is_valid_triangle(length_1, length_2, length_3):
    print("Valid")
else:
    print("Not Valid")