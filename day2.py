# 1. Is the number 10 even AND prime?(False)
# def is_even(n):
#     return n % 2 == 0

# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# n = 10

# if is_even(n) and is_prime(n):
#     print(f"The number {n} is both even AND prime.")
# else:
#     print(f"The number {n} is not both even AND prime.")


# 2. Is it raining OR snowing?(True if either is true)
# def getData(weather):
#     return input(f"is it {weather}: ").lower()
# def checking(data):
#     while not (data == "yes" or data == "no"):
#         return data
# rain = checking(getData("Raining"))
# snow = checking(getData("Snowing"))            