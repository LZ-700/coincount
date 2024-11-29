f = open("coincount.txt" "w")

print("What is your name?")
name = input("Member name: ")
f.write(name)

while True:
    cointype = input("Input Coin type: ")
    if cointype is not ["£2"]:
        print("Sorry, I didn't understand that.")
        continue
    else:
        break

print("Give the weight of the bag.")
weight = input("bag weight (g): ")
f.write(int(weight))
f.close()

