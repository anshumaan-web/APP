#Chef has his lunch only between 1 pm and 4 pm (both inclusive).
# Given that the current time is X pm, find out whether it is lunchtime for Chef.

T = int(input("Enter the number of test cases: "))
for i in range(T):
    X = int(input("Enter the time: "))
    if X >= 1 and X <= 4:
        print("YES")
    else:
        print("NO")