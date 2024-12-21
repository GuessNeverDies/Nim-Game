import random

def NIMGAME():
    pile1 = random.randint(10,100)
    pile2 = random.randint(10,100)
    playerTurn = 1 #which player's turn

    while (pile1 + pile2 >= 1):  #will repeat until one chip remaining
        print("It is Player", playerTurn, "'s turn.")
        print("There are ", pile1, "chips in pile 1.")
        print("There are ", pile2, "chips in pile 2.")

        pileChoice = input("Which pile do you want to take from? Type 1 or 2: ")
        if int(pileChoice) == 2:
            if(pile2 > 0):
                chipsToRemove = input(" How many chips would you like to take?")
                if (int(chipsToRemove) > pile2):
                    print(chipsToRemove, "is too many chips! Removing", int(pile2), "chips instead!")
                    pile2 = 0
                    playerTurn = 3 - playerTurn
                else:
                    pile2 = pile2 - int(chipsToRemove)
            elif(pile2 == 0):
                print("No more chips in pile", pileChoice)
        elif int(pileChoice) == 1:
            if(pile1 > 0):
                chipsToRemove = input(" How many chips would you like to take?")
                if (int(chipsToRemove) > pile1):
                    print(chipsToRemove, "is too many chips! Removing", int(pile1), "chips instead!")
                    pile1 = 0
                    playerTurn = 3 - playerTurn
                else:
                    pile1 = pile1 - int(chipsToRemove)
            elif(pile1 == 0):
                print("No more chips in pile", pileChoice)

        else:
            print("Error, choose either 1 or 2")

NIMGAME()


#Errors: inputing number less than 0 (negative) will add chips
#Todo: add "Player x lost"