# Run this script to create simulations of consistency
# Require functions of AI made decisions

# TO-DO LIST
# - Implement card effects
# - Run turn 1 simulations
# - Fix up card implementation
# - Implement field
# - Implement opponent information
# - Build AI past turn 1

## Blaine's to do list - Make prize cards - check
## Select them after checking for mulligans - check
## Display hand - check
## Ask the user if they want to see them - check
## Display Prize cards - check
## Implement more AI decisions - how/when to use Mysterious Treasure -
##      if 2 Mewtwo & Mew-GX is in play grab Jirachi-GX,
##      otherwise grab Mewtwo & Mew-GX - check
## Improve code of the functions - repetitions in code and efficiency (operation time) - in progress
## Display number of mulligans - check

from database import *
from effects import *
import random

# print information
def printInfo():
    # print("DECK")
    # print(playerDeck)
    print("HAND: ")
    print(playerHand)
        # Printing the discard is effective only if AI is implemented:
    # print("DISCARD")
    # print(playerDiscard)

    #Asking the user on whether they would like to view the Prize cards
    while True:
     query = input("Would you like to view your Prize cards? ")
     answer = query[0].lower()
     if query == '' or answer not in ['y','n']:
        print("Please answer with yes or no: ")
     else:
        break
    if answer == 'y':
            print("PRIZES: ")
            print(playerPrizes)
    if answer == 'n':
            print("You have selected to not view your Prize cards.")


# restarts game
def restartGame():
    playerDeck = MewMewWorlds.copy()
    playerHand = []
    playerPrizes = []
    playerDiscard = []
    active = []
    bench = []
    oppActive = []
    oppBench = []
    activeStadium = []

# sets up the game
def setUpGame():
    random.shuffle(playerDeck)
    counterCheck = drawCards(playerDeck, playerHand, 7)
    mulliganCount = 0

    # for tracking mulligans
    while (counterCheck == 0):
        shuffleCards(playerHand, playerDeck)
        random.shuffle(playerDeck)
        counterCheck = drawCards(playerDeck, playerHand, 7)
        mulliganCount += 1
    # displays number of mulligans you had before finding a Basic
    print ("Number of Mulligans: {}".format(mulliganCount))
    # sets up Prize cards after mulligans have been accounted for
    drawCards(playerDeck, playerPrizes, 6)

# draws a specified number of cards
# returns: counter check for basic
def drawCards(source, dest, number):
    counter = 0
    for i in range(0,number):  ### <-- fixed implementation to be easier/more intuitive than before (Blaine)
        card = source.pop()
        # debugging for basic
        if (card.cardType == "Pokemon"):
            if (card.stage == "Basic"):
                counter += 1
        dest.append(card)

    return counter

# shuffles hand into deck
def shuffleCards(source, dest): ## ask jeremy about shuffleCards vs shuffleEffect
    for i in range(0,len(source)):
        card = source.pop()
        dest.append(card)
    random.shuffle(dest)

def discardCard(source, card):
    if (card in source):
        source.remove(card)
        playerDiscard.append(card)

def AI_Test(consCheck):
    print("IN AI TEST")
    # print(playerHand)
    counter = 0
    suppCount = 0
    stadCount = 0
    for card in playerHand:
        if (card.cardType == "Pokemon"):
            if (card.name == "Mewtwo & Mew-GX"):
                playCard(playerHand, playerDiscard, selectCard(playerHand, card.name))
                print("MEW MEW ACTIVE")
            elif (card.name == "Mimikyu"):
                playCard(playerHand, playerDiscard, selectCard(playerHand, card.name))
                print("MIMIKYU ACTIVE")
            elif (card.name == "Mew"):
                playCard(playerHand, playerDiscard, selectCard(playerHand, card.name))
                print("MEW ACTIVE")
            elif (card.stage == "Basic"):
                playCard(playerHand, playerDiscard, selectCard(playerHand, card.name))
                print(card.name.upper() + " ACTIVE")

            break

    while (len(playerHand) > 0 and counter == 0):
        counter = 1
        if (selectCard(playerHand, "Mysterious Treasure")) and (len(playerHand)) > 1:
            if (selectCard(playerHand, "Mewtwo & Mew-GX") or ("Mewtwo & Mew-GX" in bench) or ("Mewtwo & Mew-GX" in active)): ## not sure about implementation (Blaine)
                if (len(searchEffect(playerDeck, "Jirachi-GX", "name")) > 0):
                    playCard(playerHand, playerDiscard, selectDisposableCard(playerHand))
                    addToHand(playerDeck, playerHand, selectCard(playerDeck, "Jirachi-GX"))
                    playCard(playerHand, playerDiscard, selectCard(playerHand, "Mysterious Treasure"))
                    print("MYSTERIOUS TREASURE: GOT Jirachi-GX")
            else:
                if (len(searchEffect(playerDeck, "Mewtwo & Mew-GX", "name")) > 0):
                    playCard(playerHand, playerDiscard, selectDisposableCard(playerHand))
                    addToHand(playerDeck, playerHand, selectCard(playerDeck, "Mewtwo & Mew-GX"))
                    playCard(playerHand, playerDiscard, selectCard(playerHand, "Mysterious Treasure"))
                    print("MYSTERIOUS TREASURE: GOT Mewtwo & Mew-GX")

                else:
                    print("NEITHER Jirachi-GX OR Mewtwo & Mew-GX ARE IN THE DECK. FAILED MYSTERIOUS TREASURE.")

        # Playing down Cherish Ball
        if (selectCard(playerHand, "Cherish Ball")):
            if (selectCard(playerHand, "Mewtwo & Mew-GX")):
                if (len(searchEffect(playerDeck, "Jirachi-GX", "name")) > 0):
                    addToHand(playerDeck, playerHand, selectCard(playerDeck, "Jirachi-GX"))
                    playCard(playerHand, playerDiscard, selectCard(playerHand, "Cherish Ball"))
                    print("CHERISH BALL: GOT Jirachi-GX")
                    if (selectCard(playerHand, "Jirachi-GX")):
                        playCard(playerHand, playerDiscard, selectCard(playerHand, "Jirachi-GX"))
                        print("PLAY: Jirachi-GX")
                    counter = 0

            elif (selectCard(playerHand, "Mewtwo & Mew-GX") == None):
                if (len(searchEffect(playerDeck, "Mewtwo & Mew-GX", "name")) > 0):
                    addToHand(playerDeck, playerHand, selectCard(playerDeck, "Mewtwo & Mew-GX"))
                    playCard(playerHand, playerDiscard, selectCard(playerHand, "Cherish Ball"))
                    print("CHERISH BALL: GOT Mewtwo & Mew-GX")
                    if (selectCard(playerHand, "Mewtwo & Mew-GX")):
                        playCard(playerHand, playerDiscard, selectCard(playerHand, "Mewtwo & Mew-GX"))
                        print("PLAY: Mewtwo & Mew-GX")
                    counter = 0

            if (consCheck == False):
                if (len(searchEffect(playerDeck, "Dedenne-GX", "name")) > 0):
                    addToHand(playerDeck, playerHand, selectCard(playerDeck, "Dedenne-GX"))
                    playCard(playerHand, playerDiscard, selectCard(playerHand, "Cherish Ball"))
                    print("CHERISH BALL: GOT Dedenne-GX")
                    counter = 0

        if (selectCard(playerHand, "Viridian Forest") and stadCount == 0):
            playCard(playerHand, playerDiscard, selectCard(playerHand, "Viridian Forest"))
            stadCount = 1
            print("VIRIDIAN FOREST")
            counter = 0

            # Discards a disposable card

            if(selectDisposableCard(playerHand)):
                playCard(playerHand, playerDiscard, selectDisposableCard(playerHand))
                addToHand(playerDeck, playerHand, selectCard(playerDeck, "Fire"))
                print("USING VIRIDIAN FOREST")


            # if (selectCard(playerHand, "Solgaleo-GX")):
            #     playCard(playerHand, playerDiscard, selectCard(playerHand, "Solgaleo-GX"))
            #     addToHand(playerDeck, playerHand, selectCard(playerDeck, "Fire"))
            #     print("USE VIRIDIAN FOREST")
            # elif (selectCard(playerHand, "Naganadel-GX")):
            #     playCard(playerHand, playerDiscard, selectCard(playerHand, "Naganadel-GX"))
            #     addToHand(playerDeck, playerHand, selectCard(playerDeck, "Fire"))
            #     print("USE VIRIDIAN FOREST")
            # elif (selectCard(playerHand, "Espeon & Deoxys-GX")):
            #     playCard(playerHand, playerDiscard, selectCard(playerHand, "Espeon & Deoxys-GX"))
            #     addToHand(playerDeck, playerHand, selectCard(playerDeck, "Fire"))
            #     print("USE VIRIDIAN FOREST")
            # elif (selectCard(playerHand, "Latios-GX")):
            #     playCard(playerHand, playerDiscard, selectCard(playerHand, "Latios-GX"))
            #     addToHand(playerDeck, playerHand, selectCard(playerDeck, "Fire"))
            #     print("USE VIRIDIAN FOREST")

        if (selectCard(playerHand, "Escape Board")):
            playCard(playerHand, playerDiscard, selectCard(playerHand, "Escape Board"))
            print("ESCAPE BOARD")
        if (selectCard(playerHand, "Welder") and len(searchEffect(playerHand, "Fire", "name")) >= 2 and suppCount == 0):
            playCard(playerHand, playerDiscard, selectCard(playerHand, "Welder"))
            drawEffect(playerDeck, playerHand, 3)
            suppCount = 1
            print("WELDER")
            counter = 0

        if (selectCard(playerHand, "Lillie") and suppCount == 0):
            playCard(playerHand, playerDiscard, selectCard(playerHand, "Lillie"))
            drawEffect(playerDeck, playerHand, 8 - len(playerHand))
            suppCount = 1
            print("LILLIE")
            counter = 0

# simulates consistency checks
# returns: number of consistency cards
def simulateGames(consCount):
    restartGame()
    setUpGame()
    return checkConsistency(playerHand)

# checks if you have a consistency card in hand
# returns: number of consistency cards
def checkConsistency(playerHand):
    counter = 0
    for card in playerHand:
        if (card.consCheck == True):
            counter += 1

    return counter

# runs the script
consCount = 0
for count in range(0, 20):
    consCheck = False
    playerDeck = MewMewWorlds.copy()
    playerHand = []
    playerPrizes = []
    playerDiscard = []
    active = []
    bench = []
    oppActive = []
    oppBench = []
    activeStadium = []
    outcome_of_consistency_of_game = simulateGames(consCount)
    print("GAME NO. " + str(count+1)+ " CONSISTENCY: " + str(outcome_of_consistency_of_game))
    if outcome_of_consistency_of_game > 0:
        consCount += 1
        consCheck = True

    # AI_Test(consCheck)
    # searchEffect(playerDeck, ["Psychic","Dragon"], "type")
    # printInfo()

# print("OVERALL CONSISTENCY: " + str(consCount))
# printInfo()
setUpGame()
AI_Test(consCheck)
printInfo()
