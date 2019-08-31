from random import shuffle
from pprint import pprint
deck = []
with open("source.txt") as file:
   for line in file:
       if (line.strip("\n") != ""):
            deck.append(line.strip("\n"))
 
target = set(["Exodia the Forbidden One", "Left Arm of Forbidden One", "Left Leg of the Forbidden One", "Right Arm of the Forbidden One", "Right Leg of the Forbidden One"])
tally = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, "sangan + 4": 0, 5: 0}
count = 0

while True:
    shuffle(deck)
    hand = set(deck[:5])

    count+=1

    tally[len(target.intersection(hand))] += 1
    if len(target.intersection(hand)) == 4 and 'Sangan' in hand:
        tally["sangan + 4"] += 1
        print("drew sangan+4 on hand", count, "using hand", hand)
    if len(target.intersection(hand)) == 5:
        break
    

print("total hands drawn :", count)
print("it would take", count/2, "hours to draw get this hand")
print("that's", count/2/24/7/52, "years")
pprint(tally, width=1)


           
