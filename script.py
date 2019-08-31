from random import shuffle
from pprint import pprint
deck = []
with open("source.txt") as file:
   for line in file:
       if (line.strip("\n") != ""):
            deck.append(line.strip("\n"))

flag = True   
target = set(["Exodia the Forbidden One", "Left Arm of Forbidden One", "Left Leg of the Forbidden One", "Right Arm of the Forbidden One", "Right Leg of the Forbidden One"])
sangan = target.union(set(["Sangan"]))
tally = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, "sangan + 4": 0, 5: 0}
count = 0

while flag:
    shuffle(deck)
    hand = set(deck[:5])
    tally[len(target.intersection(hand))] += 1
    if len(sangan.intersection(hand)) == 5:
        tally["sangan + 4"] += 1
    if len(target.intersection(hand)) == 5:
        break
    count+=1

print("total hands drawn:", count)
pprint(tally, width=1)


           
