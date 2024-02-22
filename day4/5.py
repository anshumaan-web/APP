#Find the missing number in the given list of integers. The list contains 1 to 100 integers but one of the integer is missing. There are no duplicates in the list.

def find_missing_number(arr):
    n = 100
    total = (n * (n + 1)) // 2
    arr_set = set(arr)
    for i in range(1, n + 1):
        if i not in arr_set:
            return i
    return None
arr = [int(i) for i in input("Enter the numbers: ").split()]
missing_number = find_missing_number(arr)
if missing_number:
    print(f"The missing number is: {missing_number}")
else:
    print("No missing number found.")