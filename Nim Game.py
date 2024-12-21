import random

pile1 = random.randint(3,8)
pile2 = random.randint(3,8)
#TODO - Create a third pile

playerID = 1


while pile1 + pile2 >= 1:  #will repeat until one chip remaining
    print("It is Player ", playerID, " 's turn.")
    print("There are ", pile1, "chips in pile 1.")
    print("There are ", pile2, "chips in pile 2.")

    pileChoice = input("Which pile do you want to take from? Type 1 or 2: ")
    chipsToRemove = input(" How many chips would you like to take?")


    if pileChoice == "1":
        pile1 = pile1 - int(chipsToRemove)

    #TODO - what if user chooses pile 2?

    if pileChoice == "2":
        pile2 = pile2 - int(chipsToRemove)

    playerID = 3 - playerID

print("Game Over! Player", playerID, "wins!")
#TODO - print result