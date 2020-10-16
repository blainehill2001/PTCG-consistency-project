# need to create objects of Pokemon cards

import random

playerDeck = []
playerHand = []
playerPrizes = []
playerDiscard = []

##### CLASS IMPLEMENTATION #####
class Card():
    def __init__(self, name, consCheck):
        self._name = name
        self._consCheck = consCheck

    @property
    def name(self):
        return self._name

    @property
    def consCheck(self):
        return self._consCheck

    def __repr__(self):
       return self._name

class Pokemon(Card):
    def __init__(self, name, type, consCheck, stage, HP, weakness, resistance, retreat, prizeLoss, disposable):
        super().__init__(name, consCheck)
        self._cardType = "Pokemon"
        self._type = type
        self._stage = stage
        self._HP = HP
        self._weakness = weakness
        self._resistance = resistance
        self._retreat = retreat
        self._prizeLoss = prizeLoss
        self._attached = []
        self._disposable = disposable


    @property
    def cardType(self):
        return self._cardType

    @property
    def type(self):
        return self._type

    @property
    def stage(self):
        return self._stage

    @property
    def HP(self):
        return self._HP

    @property
    def weakness(self):
        return self._weakness

    @property
    def resistance(self):
        return self._resistance

    @property
    def retreat(self):
        return self._retreat

    @property
    def prizeLoss(self):
        return self._prizeLoss

    @property
    def attached(self):
        return self._attached

    @property
    def disposable(self):
        return self._disposable

class Trainer(Card):
    def __init__(self, name, consCheck):
        super().__init__(name, consCheck)

    pass

class Item(Trainer):
    def __init__(self, name, consCheck, cardDraw, thinDraw, thinCheck, effects, priority, disposable):
        super().__init__(name, consCheck)
        self._cardType = "Item"
        self._cardDraw = cardDraw
        self._thinDraw = thinDraw
        self._thinCheck = thinCheck
        self._effects = effects
        self._priority = priority
        self._disposable = disposable

    @property
    def cardType(self):
        return self._cardType

    @property
    def cardDraw(self):
        return self._cardDraw

    @property
    def thinDraw(self):
        return self._thinDraw

    @property
    def thinCheck(self):
        return self._thinCheck

    @property
    def effects(self):
        return self._effects

    @property
    def priority(self):
        return self._priority

    @property
    def disposable(self):
        return self._disposable

    def play(effects):
        for condition in effects:
            pass

class Supporter(Trainer):
    def __init__(self, name, consCheck, cardDraw, thinDraw, thinCheck, priority, disposable):
        super().__init__(name, consCheck)
        self._cardType = "Supporter"
        self._cardDraw = cardDraw
        self._thinDraw = thinDraw
        self._thinCheck = thinCheck
        self._priority = priority
        self._disposable = disposable

    @property
    def cardType(self):
        return self._cardType

    @property
    def cardDraw(self):
        return self._cardDraw

    @property
    def thinDraw(self):
        return self._thinDraw

    @property
    def thinCheck(self):
        return self._thinCheck

    @property
    def priority(self):
        return self._priority

    @property
    def disposable(self):
        return self._disposable

class Stadium(Trainer):
    def __init__(self, name, consCheck, cardDraw, thinDraw, thinCheck, priority, disposable):
        super().__init__(name, consCheck)
        self._cardType = "Stadium"
        self._cardDraw = cardDraw
        self._thinDraw = thinDraw
        self._thinCheck = thinCheck
        self._priority = priority
        self._disposable = disposable
    @property
    def cardType(self):
        return self._cardType

    @property
    def cardDraw(self):
        return self._cardDraw

    @property
    def thinDraw(self):
        return self._thinDraw

    @property
    def thinCheck(self):
        return self._thinCheck

    @property
    def priority(self):
        return self._priority

    @property
    def disposable(self):
        return self._disposable

class Energy(Card):
    def __init__(self, name, consCheck, disposable):
        super().__init__(name, consCheck)
        self._cardType = "Energy"
        self._disposable = disposable

    @property
    def cardType(self):
        return self._cardType

    @property
    def disposable(self):
        return self._disposable

class Field():
    def __init__(self, active, bench, oppActive, oppBench, activeStadium):
        self._active = active
        self._bench = bench
        self._oppActive = oppActive
        self._oppBench = oppBench
        self._activeStadium = activeStadium

    @property
    def active(self):
        return self._active

    @property
    def bench(self):
        return self._bench

    @property
    def oppActive(self):
        return self._oppActive

    @property
    def oppBench(self):
        return self._oppBench

    @property
    def activeStadium(self):
        return self._activeStadium

################################################################################

# PokemonDB = [
#     Pokemon("Inkay","Psychic", False, "Basic", 60, "Psychic", None, 1, 1),
#     Pokemon("Malamar","Psychic", False, "Stage 1", 90, "Psychic", None, 2, 1),
#     Pokemon("Giratina","Psychic", False, "Basic", 130, "Psychic", None, 3, 1),
#     Pokemon("Jirachi","Psychic", False, "Basic", 70, "Metal", "Psychic", 1, 1),
#     Pokemon("Ditto Prism Star","Colorless", False, "Basic", 40, "Fighting", None, 1, 1),
#     Pokemon("Mimikyu","Psychic", False, "Basic", 70, "Psychic", None, 1, 1),
#     Pokemon("Espurr","Psychic", False, "Basic", 60, "Psychic", None, 1, 1),
#     Pokemon("Espeon & Deoxys-GX","Psychic", False, "Basic", 260, "Psychic", None, 2, 3),
#     Pokemon("Ultra Necrozma-GX","Psychic", False, "Basic", 60, "Fairy", None, 2, 2),
#     Pokemon("Dedenne-GX","Lightning", True, "Basic", 160, "Fighting", None, 1, 2)
# ]
#
# MalamarWorlds = [
#     Pokemon("Inkay","Psychic", False, "Basic", 60, "Psychic", None, 1, 1),
#     Pokemon("Inkay","Psychic", False, "Basic", 60, "Psychic", None, 1, 1),
#     Pokemon("Inkay","Psychic", False, "Basic", 60, "Psychic", None, 1, 1),
#     Pokemon("Inkay","Psychic", False, "Basic", 60, "Psychic", None, 1, 1),
#     Pokemon("Malamar","Psychic", False, "Stage 1", 90, "Psychic", None, 2, 1),
#     Pokemon("Malamar","Psychic", False, "Stage 1", 90, "Psychic", None, 2, 1),
#     Pokemon("Malamar","Psychic", False, "Stage 1", 90, "Psychic", None, 2, 1),
#     Pokemon("Malamar","Psychic", False, "Stage 1", 90, "Psychic", None, 2, 1),
#     Pokemon("Giratina","Psychic", False, "Basic", 130, "Psychic", None, 3, 1),
#     Pokemon("Giratina","Psychic", False, "Basic", 130, "Psychic", None, 3, 1),
#     Pokemon("Jirachi","Psychic", True, "Basic", 70, "Metal", "Psychic", 1, 1),
#     Pokemon("Jirachi","Psychic", True, "Basic", 70, "Metal", "Psychic", 1, 1),
#     Pokemon("Jirachi","Psychic", True, "Basic", 70, "Metal", "Psychic", 1, 1),
#     Pokemon("Ditto Prism Star","Colorless", False, "Basic", 40, "Fighting", None, 1, 1),
#     Pokemon("Mew","Psychic", False, "Basic", 60, "Psychic", None, 1, 1),
#     Pokemon("Mimikyu","Psychic", False, "Basic", 70, "Psychic", None, 1, 1),
#     Pokemon("Espurr","Psychic", False, "Basic", 60, "Psychic", None, 1, 1),
#     Pokemon("Espeon & Deoxys-GX","Psychic", False, "Basic", 260, "Psychic", None, 2, 3),
#     Pokemon("Ultra Necrozma-GX","Psychic", False, "Basic", 60, "Fairy", None, 2, 2),
#     Pokemon("Dedenne-GX","Lightning", True, "Basic", 160, "Fighting", None, 1, 2),
#     Supporter("Lillie", True, 8, 0, True, 2),
#     Supporter("Lillie", True, 8, 0, True, 2),
#     Supporter("Lillie", True, 8, 0, True, 2),
#     Supporter("Lillie", True, 8, 0, True, 2),
#     Supporter("Cynthia", True, 6, 0, True, 2),
#     Supporter("Cynthia", True, 6, 0, True, 2),
#     Supporter("Cynthia", True, 6, 0, True, 2),
#     Supporter("Cynthia", True, 6, 0, True, 2),
#     Item("Mysterious Treasure", False, 0, 1, False, 7),
#     Item("Mysterious Treasure", False, 0, 1, False, 7),
#     Item("Mysterious Treasure", False, 0, 1, False, 7),
#     Item("Mysterious Treasure", False, 0, 1, False, 7),
#     Item("Pokemon Communication", True, 0, 0, False, 5),
#     Item("Pokemon Communication", True, 0, 0, False, 5),
#     Item("Pokemon Communication", True, 0, 0, False, 5),
#     Item("Pokemon Communication", True, 0, 0, False, 5),
#     Item("Acro Bike", False, 1, 1, True, 8),
#     Item("Acro Bike", False, 1, 1, True, 8),
#     Item("Acro Bike", False, 1, 1, True, 8),
#     Item("Switch", False, 0, 0, False, 1),
#     Item("Switch", False, 0, 0, False, 1),
#     Item("Switch", False, 0, 0, False, 1),
#     Item("Spell Tag", False, 0, 0, False, 3),
#     Item("Spell Tag", False, 0, 0, False, 3),
#     Item("Spell Tag", False, 0, 0, False, 3),
#     Item("Spell Tag", False, 0, 0, False, 3),
#     Item("Escape Board", False, 0, 0, False, 3),
#     Item("Escape Board", False, 0, 0, False, 3),
#     Stadium("Viridian Forest", False, 0, 1, True, 6),
#     Stadium("Viridian Forest", False, 0, 1, True, 6),
#     Stadium("Viridian Forest", False, 0, 1, True, 6),
#     Energy("Psychic", False),
#     Energy("Psychic", False),
#     Energy("Psychic", False),
#     Energy("Psychic", False),
#     Energy("Psychic", False),
#     Energy("Psychic", False),
#     Energy("Psychic", False),
#     Energy("Psychic", False),
#     Energy("Metal", False)
# ]

MewMewWorlds = [
    Pokemon("Mewtwo & Mew-GX", "Psychic", False, "Basic", 270, "Psychic", None, 2, 3, False),
    Pokemon("Mewtwo & Mew-GX", "Psychic", False, "Basic", 270, "Psychic", None, 2, 3, False),
    Pokemon("Mewtwo & Mew-GX", "Psychic", False, "Basic", 270, "Psychic", None, 2, 3, False),
    Pokemon("Mewtwo & Mew-GX", "Psychic", False, "Basic", 270, "Psychic", None, 2, 3, False),
    Pokemon("Dedenne-GX", "Lightning", True, "Basic", 160, "Fighting", None, 1, 2, False),
    Pokemon("Dedenne-GX", "Lightning", True, "Basic", 160, "Fighting", None, 1, 2, False),
    Pokemon("Reshiram & Charizard-GX", "Fire", False, "Basic", 270, "Water", None, 3, 3, True),
    Pokemon("Espeon & Deoxys-GX", "Psychic", False, "Basic", 260, "Psychic", None, 2, 3, True),
    Pokemon("Solgaleo-GX", "Metal", False, "Stage 2", 250, "Fire", "Psychic", 3, 2, True),
    Pokemon("Naganadel-GX", "Dragon", False, "Stage 1", 210, "Fairy", None, 1, 2, True),
    Pokemon("Latios-GX", "Psychic", False, "Basic", 170, "Psychic", None, 0, 2, True),
    Pokemon("Jirachi-GX", "Psychic", False, "Basic", 160, "Psychic", None, 1, 2, False),
    Pokemon("Mew", "Psychic", False, "Basic", 60, "Psychic", None, 1, 1, False),
    Pokemon("Mimikyu", "Psychic", False, "Basic", 70, "Psychic", None, 1, 1, False),
    Supporter("Welder", True, 3, 0, True, 4, False),
    Supporter("Welder", True, 3, 0, True, 4, False),
    Supporter("Welder", True, 3, 0, True, 4, False),
    Supporter("Welder", True, 3, 0, True, 4, False),
    Supporter("Lillie", True, 8, 0, True, 2, False),
    Supporter("Lillie", True, 8, 0, True, 2, False),
    Supporter("Lillie", True, 8, 0, True, 2, False),
    Supporter("Lillie", True, 8, 0, True, 2, False),
    Item("Cherish Ball", True, 0, 1, False, None, 5, False),
    Item("Cherish Ball", True, 0, 1, False, None, 5, False),
    Item("Cherish Ball", True, 0, 1, False, None, 5, False),
    Item("Cherish Ball", True, 0, 1, False, None, 5, False),
    Item("Acro Bike", False, 1, 1, True, None, 8, False),
    Item("Acro Bike", False, 1, 1, True, None, 8, False),
    Item("Acro Bike", False, 1, 1, True, None, 8, False),
    Item("Acro Bike", False, 1, 1, True, None, 8, False),
    Item("Mysterious Treasure", False, 0, 1, False, None, 7, False),
    Item("Mysterious Treasure", False, 0, 1, False, None, 7, False),
    Item("Mysterious Treasure", False, 0, 1, False, None, 7, False),
    Item("Mysterious Treasure", False, 0, 1, False, None, 7, False),
    Item("Custom Catcher", False, 3, 0, True, None, 1, True),
    Item("Custom Catcher", False, 3, 0, True, None, 1, True),
    Item("Custom Catcher", False, 3, 0, True, None, 1, True),
    Item("Custom Catcher", False, 3, 0, True, None, 1, True),
    Stadium("Viridian Forest", False, 0, 1, True, 6, True),
    Stadium("Viridian Forest", False, 0, 1, True, 6, True),
    Stadium("Viridian Forest", False, 0, 1, True, 6, True),
    Stadium("Viridian Forest", False, 0, 1, True, 6, True),
    Item("Escape Board", False, 0, 0, False, None, 3, True),
    Item("Escape Board", False, 0, 0, False, None, 3, True),
    Item("Escape Board", False, 0, 0, False, None, 3, True),
    Item("Reset Stamp", False, 0, 0, False, None, 2, True),
    Item("Reset Stamp", False, 0, 0, False, None, 2, True),
    Item("Reset Stamp", False, 0, 0, False, None, 2, True),
    Energy("Fire", False, True),
    Energy("Fire", False, True),
    Energy("Fire", False, True),
    Energy("Fire", False, True),
    Energy("Fire", False, True),
    Energy("Fire", False, True),
    Energy("Fire", False, True),
    Energy("Fire", False, True),
    Energy("Psychic", False, True),
    Energy("Psychic", False, True),
    Energy("Psychic", False, True),
    Energy("Psychic", False, True),
]

################################################################################

##### DICTIONARY IMPLEMENTATION #####

# PokemonDB = [{
#     "name"
# }]

# Pokemon
# Item
# Supporter
# Stadium
# Energy
