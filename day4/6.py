#Given a number N, reverse the number.

def reverse_num(num):
    rev_num = 0
    while num > 0:
        rem = num % 10
        rev_num = rev_num * 10 + rem
        num = num // 10
    return rev_num
num = int(input("Enter the number: "))
print("Reverse of", num, "is", reverse_num(num))