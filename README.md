# PTCG-consistency-project
This is a utilitarian program to quickly test the consistency of a Pokemon TCG deck, by Blaine Hill -- Fall 2020

In the Pokemon TCG, each deck that a player battles with consists of 60 cards with three types of cards: Pokemon, Trainers, and Energy. Certain Pokemon are geared to battle, while others have interactions with the battlefield. Trainer cards are the bread and butter to executing one's strategy: they can draw more cards, manipulate Energy, and even boost the power of a Pokemon! Energy cards are the simpliest, but most necessary piece to deck as they allow for Pokemon to battle.

Consistency is a metric that is used by top Pokemon TCG players to evaluate the strength of a deck; a high consistency correlates to higher performances at tournaments. Though there is no concrete definition, it is generally agreed upon that consistency refers to the probability of how often a deck's ideal strategy can be accomplished.

In this project, though I have not been able to simulate an entire Pokemon TCG game between two autonomous agents (yet!), I've created a simulation to compute consistency given a 60-card deck. Each card is marked as an "out" or not meaning that it can draw the player more cards. Then the first turn of the game is simulated. After many iterations, an average consistency metric is calculated.

Going forward, this project could eventually make use of official PTCGO data - a platform for playing the PTCG online. It would be extremely interesting from a successful player's perspective to train a few AI models on it, similar to AlphaZero or AlphaGo, teaching a model how to play the game and viewing how it learns and plays.
