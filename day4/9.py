#Chef is not feeling well today. He measured his body temperature using a thermometer and it came out to be X °F.
# A person is said to have fever if his body temperature is strictly greater than 98°F.
# Determine if Chef has fever or not.

T = int(input("No of test cases: "))
for i in range(T):
    X = int(input("Enter the temprature: "))
    if X > 98:
        print("YES fever detected.")
    else:
        print("NO fever not detected.")