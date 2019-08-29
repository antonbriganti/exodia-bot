from random import shuffle
deck = []
with open("source.txt") as file:
   for line in file:
       if (line.strip("\n") != ""):
            deck.append(line.strip("\n"))

flag = True   
target = ["Exodia the Forbidden One", "Left Arm of Forbidden One", "Left Leg of the Forbidden One", "Right Arm of the Forbidden One", "Right Leg of the Forbidden One"]

count = 0
while flag:
    shuffle(deck)
    hand = deck[:5]
    # change to sets, use to call out when something's close/got one piece
    if target == sorted(hand):
        print(count)
        break
    count+=1


           
