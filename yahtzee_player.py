import random
from yahtzee_calc import Yahtzee_calc

# ABSTRACTION - the player is a person but the player here is only the data associated with a single turn
# ENCAPSULATION - each instance is a single turn of play

class Yahtzee_player:

    def __init__(self, player_name, player_type, game_status, dice_roll):
        self._player_name = player_name
        self._player_type = player_type
        self._game_status = game_status
        self._dice_roll = dice_roll
        
    def player_turn(self):
        if self.player_type == "computer":
            self._dice.roll = [random.randrange(1, 7) for i in range(0, 5)]
    
    def calculate_score(self):
        # create an instance to send to the calculator
        variable =  Yahtzee_calc(self._dice_roll)
        return variable
    
        
if __name__ == "__main__":
    # create 1 player instance of a turn of play for a computer
    computer1 = Yahtzee_player("C1", "computer", {}, [])
    
    print(computer1.calculate_score())