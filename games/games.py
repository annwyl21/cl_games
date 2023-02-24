# My encapsulation of a game
import sys, time

class Games: # defining a datatype of game

    def __init__(self, name): # initialising an instance and adding instance variables
        self._name = name
        

    def set_title(self, title): # setter
        self._title = title

    def get_title(self):
        return self._title
    
    def end_game(end_game_message): # static method
        print(end_game_message, '\n', "="*50)
        sys.exit()

    def open_game(self, game_name_list): # static method
        for item in game_name_list:
            time.sleep(0.85)
            print(item, end = '', flush = True)
        

class Player:

    def __init__(self, opening_score):
        self._score = opening_score

    # BEHAVIOUR
    def increase_score(self, points):
        self._score += points
    
    # getter DATA
    def get_score(self):
        return self._score

