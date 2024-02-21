def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

num = int(input("Enter the number: "))

if is_even(num):
    print(f"{num} is an even number.")
else:
    print(f"{num} is an odd number.")

if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
