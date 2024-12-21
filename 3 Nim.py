import random


pile1 = random.randint(3, 8)
pile2 = random.randint(3, 8)
pile3 = random.randint(3, 8)
# TODO - Create a third pile

playerID = 1


while pile1 + pile2 + pile3 >= 1:  # will repeat until one chip remaining
    print("It is Player ", playerID, " 's turn.")
    print("There are ", pile1, "chips in pile 1.")
    print("There are ", pile2, "chips in pile 2.")
    print("There are ", pile3, "chips in pile 3.")

    pileChoice = input("Which pile do you want to take from? Type 1, 2, or 3: ")
    if pileChoice == "1" or pileChoice == "2" or pileChoice == "3":
        chipsToRemove = input(" How many chips would you like to take?")
        if "1" <= chipsToRemove <= "8":  # checks to see if the chips to remove value is allowed
            if pileChoice == "1":
                if pile1 == 0:
                    pile1 = 0
                    pile2 = 0
                    pile3 = 0
                if int(chipsToRemove) > pile1:
                    print(chipsToRemove, "is too many chips! Removing", pile1, "chips instead!")  # This ensures no negatives
                    pile1 = 0
                else:
                    pile1 = pile1 - int(chipsToRemove)
            if pileChoice == "2":
                if pile2 == 0:
                    pile1 = 0
                    pile2 = 0
                    pile3 = 0
                if int(chipsToRemove) > pile2:
                    print(chipsToRemove, "is too many chips! Removing", pile2, "chips instead!")
                    pile2 = 0
                else:
                    pile2 = pile2 - int(chipsToRemove)

            if pileChoice == "3":
                if pile3 == 0:
                    pile1 = 0
                    pile2 = 0
                    pile3 = 0
                if int(chipsToRemove) > pile3:
                    print(chipsToRemove, "is too many chips! Removing", pile3, "chips instead!")
                    pile3 = 0
                else:
                    pile3 = pile3 - int(chipsToRemove)
            playerID = 3 - playerID
        else:  # if the chips is an invalid entry, this will run
            print("Do you feel good about breaking this game? This was meant for a school project, and you just broke it.")
            pile1 = 0
            pile2 = 0
            pile3 = 0
            playerID = 3 - playerID
    else:
        print("Self destruct sequence has commenced...")
        pile1 = 0
        pile2 = 0
        pile3 = 0
        playerID = 3 - playerID

# TODO - Fix if chips = 0 in pile but can just skip turn

print("Game Over! Player", playerID, "wins!")
