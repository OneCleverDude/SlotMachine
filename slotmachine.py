#
# Slot Machine
#
######################################################
#
print("Welcome to the Slot Machine!")
numberOfTimes = input('How many times do you want to play?')
slotsPossible = ["bar","bar","bar","cherry","crown"]
Loser = ["\nFEED ME MORE MONEY", "\nYa lose", "\nThanks dood", "\nHow's that retirement fund looking?"]
#
# This part builds an array of possible answers.
# (the are also called "elements" of the array.
# You can try adding or removing things to this list.
#
######################################################
#
from random import *
#
# This part loads random so we can use choice later.
# Imports are a really neat part of Python, and we'll
# talk more about them later, but for now, just know that
# we're getting all of the things that random has.
# (that's what the asterick does, grabs all of the things.)
#
######################################################
#
def play():
    slot1=choice(slotsPossible)
    slot2=choice(slotsPossible)
    slot3=choice(slotsPossible)
    sassyLoss = choice(Loser)
    win = sassyLoss
    #
    # Here we set up three slot by naming three variables as
    # slot1, slot2, and slot3.  If we wanted more, we would just
    # need a slot4, slot5, and so on.
    #
    # the choice() function is from random that we imported
    # above and that function will get one (and only one) of
    # the possible elements on the array we built above.
    #
    ######################################################
    #
    if (slot1==slot2==slot3=="cherry"):
        win = "\nYou win $100"
    if (slot1==slot2==slot3=="crown"):
        win = "\nYou win $50"
    if (slot1==slot2==slot3=="bar"):
        win = "\nYou win $5"
    return slot1+":"+slot2+":"+slot3+" "+win
    #
    # Here is where we decide if you won.  We check to see
    # if the three slot variables are all equivilant (remember
    # that you want equilivant (==) not an assignment (=).
    # when they are all equilivant and match the last string, then
    # we do something with it.  In this case, we return it to be printed.
    #
    ######################################################
for i in range(int(numberOfTimes)):
    print(play())
    
#we should add a tracker for winnings
