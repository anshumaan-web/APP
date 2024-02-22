#Chef considers the climate HOT if the temperature is above 20, otherwise he considers it COLD. 
# You are given the temperature C, find whether the climate is HOT or COLD.

T = int(input("Enter the number of test cases: "))
for i in range(T):
    C = float(input("Enter the temprature: "))
    if C > 20:
        print("HOT")
    else:
        print("COLD")