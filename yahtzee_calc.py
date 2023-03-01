import random

# ABSTRACTION: the calculator is only calculating the possible scores from a sinlge dice roll, it is not concerned with the bonus or state of play of the game
# ENCAPSULATION: each instance is an encapsulation of a single dice roll 

# call calculator() to run and return the score dictionary

class Yahtzee_calc:
    
    def __init__(self, dice_roll):
        self._dice_roll = sorted(dice_roll)
        self._score_dict = {}

    def get_dice_roll(self):
        return self._dice_roll
        
    def dice_count(self):
        dice_count = [self._dice_roll.count(face_value) for face_value in range(1,7)]
        return dice_count
    
    def update_scores(self):
        self._upper_score = self.calculate_upper_score()
        self._lower_score = self.calculate_lower_score()
        for label, score in self._upper_score.items():
            if score > 0:
                self._score_dict[label] = score
        for label, score in self._lower_score.items():
            if score > 0:
                self._score_dict[label] = score
        return self._score_dict

    def get_score_dict(self):
        return self._score_dict
    
    # call calculator to run and return the score dictionary
    def calculator(self):
        return self.update_scores()
        
    def calculate_upper_score(self):
        scores = [self._dice_roll.count(i) *i for i in range(1,7)]
        upper_score_names = ["aces", "twos", "threes", "fours", "fives", "sixes"]
        upper_score_dict = {}
        for num, name in enumerate(upper_score_names):
            upper_score_dict[name] = scores[num]
        return upper_score_dict

    def calculate_lower_score(self):
        
        lower_score_dict = {}
        dice_set = set(self._dice_roll)
        dice_set_length = len(dice_set)
        
        # score yahtzee, full house, four of a kind, large straight
        if dice_set_length == 1:
            lower_score_dict["yahtzee"] = 50
        elif dice_set_length == 2:
            if 3 in self.dice_count() and 2 in self.dice_count():
                lower_score_dict["full_house"] = 25
            elif 4 in self.dice_count():
                kind_four = [4*i for i in range(0,7) if self._dice_roll.count(i) == 4]
                lower_score_dict["four_of_a_kind"] = kind_four[0]
        
        # score three of a kind
        if 3 in self.dice_count():
            kind_three = [3*i for i in range(0,7) if self._dice_roll.count(i) == 3]
            lower_score_dict["three_of_a_kind"] = kind_three[0]
        
        # score small & large straight
        matches = 0
        if dice_set_length >= 4:
            matches1 = 0
            matches2 = 0
            matches3 = 0
            for cycle in range(1, 4):
                for num, face_value in enumerate(dice_set, cycle):
                    if num == face_value and cycle == 1:
                        matches1 += 1
                        if matches1 > matches:
                            matches = matches1
                    elif num == face_value and cycle == 2:
                        matches2 += 1
                        if matches2 > matches:
                            matches = matches2
                    elif num == face_value and cycle == 3:
                        matches3 += 1
                        if matches3 > matches:
                            matches = matches3      
            if matches == 5:
                lower_score_dict["lg_straight"] = 40
            elif matches == 4:
                lower_score_dict["sm_straight"] = 30

        # chance score
        lower_score_dict["chance"] = sum(self._dice_roll)
        return lower_score_dict


if __name__ == "__main__":
    # create a random dice roll
    computer_dice_roll = [random.randrange(1, 7) for i in range(0, 5)]
    # create a single instance of a turn of play using the dice roll and call it the computers turn
    computer = Yahtzee_calc(computer_dice_roll)

    #print ("test", computer.calculator())
    print("overall result", computer.calculator())