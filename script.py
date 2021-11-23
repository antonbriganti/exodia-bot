from random import shuffle
from pprint import pprint

def create_deck_from_file(file_location):
    deck = []

    with open(file_location) as file:
        for line in file:
            if (line.strip("\n") != ""):
                    deck.append(line.strip("\n"))
    
    return deck

def print_results(tally, total_hands_drawn):
    print()
    print("-- results --")
    print("total hands drawn :", total_hands_drawn)
    print("it would take", total_hands_drawn/2, "hours to draw get this hand")
    print("that's", total_hands_drawn/2/24/7/52, "years")
    pprint(tally, width=1)

deck = create_deck_from_file("source.txt")
target = set(["Exodia the Forbidden One", "Left Arm of Forbidden One", "Left Leg of the Forbidden One", "Right Arm of the Forbidden One", "Right Leg of the Forbidden One"])
exodia_hands_draw_tally = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, "sangan + 4": 0, 5: 0}
total_hands_drawn = 0

print("-- starting exodia bot --")

while True:
    total_hands_drawn+=1
    
    shuffle(deck)
    hand = set(deck[:5])

    amount_of_exodia_cards_drawn = len(target.intersection(hand))

    exodia_hands_draw_tally[amount_of_exodia_cards_drawn] += 1
    
    if amount_of_exodia_cards_drawn == 4 and 'Sangan' in hand:
        exodia_hands_draw_tally["sangan + 4"] += 1
        print("drew sangan+4 on hand", total_hands_drawn, "using hand", hand, " -- ", total_hands_drawn/2, "hours /", total_hands_drawn/2/24/7/52, "years")
    
    if amount_of_exodia_cards_drawn == 5:
        break

print_results(exodia_hands_draw_tally, total_hands_drawn)