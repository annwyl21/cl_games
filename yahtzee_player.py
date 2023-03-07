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

    def calculate_computer_score(self):
        # create a random dice roll for the computer
        self._dice_roll = [random.randrange(1, 7) for i in range(0, 5)]
        
        # create an instance to send to the calculator mehod in the calc class
        self._score_dictionary = Yahtzee_calc(self.get_dice_roll()).calculator()
        #print(self._player_name.get_score_dict())

        # update computer score with either highest score or a score higher than zero
        highest_score = 0
        for roll_type, score in self._score_dictionary.items():
            if score > highest_score:
                highest_score = score
                if self._game_dictionary[roll_type] == 0:
                    self._game_dictionary[roll_type] = score
            else:
                for myref, number in self._score_dictionary.items():
                    if number > 0:
                        for stored_results in self._game_dictionary.values():
                            if stored_results == 0:
                                self._game_dictionary[myref] = number
        return self._score_dictionary
        
    def calculate_player_score(self):
        pass
    #     # calculate the score using the players dice roll
    #     self._score_dictionary = Yahtzee_calc(self._dice_roll).calculator()

    #     # display the score choices
    #     print("Here are the possible scores available from your dice roll...")
    #     print("Number to pick result - Results to choose from - Current Game Scores Held")
    #     for key, value in enumerate()



    def player_turn(self):
        if self._player_type == "computer":
            self._score_dictionary = self.calculate_computer_score()
        else:
            self._score_dictionary = self.calculate_player_score()
        return self._score_dictionary

        
if __name__ == "__main__":
    # create 1 player instance of a turn of play for a computer
    computer1 = Yahtzee_player("computer", [])
    
    print(computer1.player_turn())
    print(computer1.get_dice_roll())

    # computer turn not working