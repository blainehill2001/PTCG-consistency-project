from database import *
import random

##### EFFECT IMPLEMENTATION #####
def selectCard(source, target):
    card = next(filter(lambda card: card.name == target, source), None)
    return card

def selectDisposableCard(source):
    card = next(filter(lambda card: card.disposable == True, source), None)
    return card

def playCard(source, dest, card):
    source.remove(card)
    dest.append(card)

def drawEffect(source, dest, number):
    for i in source:
        number_in_source += 1
    number = min([number_in_source, number])

    for i in range(0, number):
        card = source.pop()
        dest.append(card)

def addToHand(source, dest, card):
    source.remove(card)
    dest.append(card)

# searches source for a card
# returns: list of possible targets
def searchEffect(source, target, attr):
    if (attr == "name"):
        searched = list(filter(lambda card: card.name == target, source))
    elif (attr == "type"):
        searched = list(filter(lambda card: card.cardType == "Pokemon", source))
        searched = list(filter(lambda card: card.type == target, searched))
    elif (attr == "stage"):
        searched = list(filter(lambda card: card.cardType == "Pokemon", source))
        searched = list(filter(lambda card: card.stage == target, searched))
    elif (attr == "cardType"):
        searched = list(filter(lambda card: card.cardType == target, source))
    elif (attr == "GX"):
        searched = list(filter(lambda card: card.cardType == "Pokemon", source))
        searched = list(filter(lambda card: card.prizeLoss == 2 or card.prizeLoss == 3, searched))
        if (target != None):
            searched = list(filter(lambda card: card.name == target, searched))
    elif (attr == "Tag Team"):
        searched = list(filter(lambda card: card.cardType == "Pokemon", source))
        searched = list(filter(lambda card: card.prizeLoss == 3, searched))
        if (target != None):
            searched = list(filter(lambda card: card.name == target, searched))

    # print(searched)
    return searched

def shuffleEffect(source, dest):
    for i in range(0,len(source)):
        card = source.pop()
        dest.append(card)
    random.shuffle(dest)

def shuffleCard(source, dest, card): #################### ask jeremy
    card = selectCard(source, card)
    source.remove(card)
    dest.append(card)


def chooseEffect(source, number, attr):

    pass
