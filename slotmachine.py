print("Welcome to the Slot Machine!")
numberOfTimes = input('How many times do you want to play?')
slotsPossible = ["bar","bar","bar","cherry","crown"]
Loser = ["\nFEED ME MORE MONEY", "\nYa lose", "\nThanks dood", "\nHow's that retirement fund looking?"]
from random import *
def play():
    slot1=choice(slotsPossible)
    slot2=choice(slotsPossible)
    slot3=choice(slotsPossible)
    sassyLoss = choice(Loser)
    win = sassyLoss
    if (slot1==slot2==slot3=="cherry"):
        win = "\nYou win $100"
    if (slot1==slot2==slot3=="crown"):
        win = "\nYou win $50"
    if (slot1==slot2==slot3=="bar"):
        win = "\nYou win $5"
    return slot1+":"+slot2+":"+slot3+" "+win
for i in range(int(numberOfTimes)):
    print(play())
