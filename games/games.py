# ABSTRACTION - the object here is the score that I need to track through the game for both player and computer and not the game title etc
# ENCAPSULATION - the score tracker is encapsulated here so it is not dragged through functions and over complicating the game
import sys, time

class Games: # defining a datatype of game

    def __init__(self, opening_score):
        self._score = opening_score

    # BEHAVIOUR
    def increase_score(self, points):
        self._score += points
    
    # getter DATA
    def get_score(self):
        return self._score

