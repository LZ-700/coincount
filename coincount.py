


f= open("coincount.txt" "w")

print("What is your name?")
n = input("Member name: ")
f.write(n)

P = True
while P:
    print("Input coin type.")
    c = input("Coin type: ")
#if c is not 
f.write(c)

print("Give the weight of the bag.")
w = input("bag weight (g): ")
f.write(int(w))
f.close()

