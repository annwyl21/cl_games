import random
from yahtzee_calc import Yahtzee_calc

# ABSTRACTION - the player is a person or a computer but the abstraction here is only the data associated with a single turn
# ENCAPSULATION - each instance is a single turn of play

# call calculate_score() to run and return the score dictionary

class Yahtzee_player:

    def __init__(self, player_type, dice_roll):
        self._player_type = player_type
        self._dice_roll = dice_roll
        self._game_dictionary = {"aces": 0,
                             "twos": 0,
                             "threes": 0,
                             "fours": 0,
                             "fives": 0,
                             "sixes": 0,
                             "three_of_a_kind": 0,
                             "four_of_a_kind": 0,
                             "full_house": 0,
                             "sm_straight": 0,
                             "lg_straight": 0,
                             "yahtzee": 0
                             }
         
    def get_dice_roll(self):
        return self._dice_roll
    
    def player_turn(self):
        if self._player_type == "computer":
            self._dice_roll = [random.randrange(1, 7) for i in range(0, 5)]
        self.update_computer_turn()
    
    def update_computer_turn():
        for score in self._
    
    def calculate_score(self):
        # determine player_type & random dice roll so never call this more than once!
        self.player_turn()
        # create an instance to send to the calculator
        self._score_dictionary = Yahtzee_calc(self._dice_roll).calculator()
        #print(self._player_name.get_score_dict())

        # update computer score
        highest_score = 0
        for key, score in self._score_dictionary.items():
            if score > highest_score:
                highest_score = score
                if self._game_dictionary[key] == 0:
                    self._game_dictionary[key] = score

        return self._score_dictionary

        
if __name__ == "__main__":
    # create 1 player instance of a turn of play for a computer
    computer1 = Yahtzee_player("computer", [])
    
    print(computer1.calculate_score())
    print(computer1.get_dice_roll())