#Write a program which prints small/large/equal relation of given two integers a and b.

def compare_numbers(a, b):
    if a < b:
        print("a < b")
    elif a > b:
        print("a > b")
    else:
        print("a == b")
a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))
compare_numbers(a, b)