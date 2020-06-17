score = input("Enter Score: ")
s = float(score)
if 0.0 <= s <= 1.0:
    if s >= 0.9:
        print ("A")
    if 0.8 <= s < 0.9:
        print ("B")
    if 0.7 <= s <= 0.8:
        print ("C")
    if 0.6 <= s <= 0.7:
        print ("D")
    if s < 0.6:
        print("F")
else: print("Error")

score = input("Enter Score: ")
s = float(score)
if s > 1.0:
    print("Error")
elif s >= 0.9:
    print("A")
elif s >= 0.8:
    print("B")