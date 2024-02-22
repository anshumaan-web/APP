#(n) school children divide (k) apples evenly, the residue remains in the basket. How many apples remains in the basket?

n = int(input("Enter the number of children: "))
k = int(input("Enter the number of apples: "))
rem = k % n
print("The  remaining number of apples after distribution is", rem)