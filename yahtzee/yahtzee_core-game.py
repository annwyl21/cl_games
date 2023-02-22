import random

r_dict = {"Aces": 0, "Twos": 0, "Threes": 0, "Fours": 0, "Fives": 0, "Sixes": 0, "Three of a kind": 0, "Four of a kind": 0, "Full House": 0, "SM Straight": 0, "LG Straight": 0, "YAHTZEE": 0, "Chance": 0}

def cl_display(dice_roll):
    print(f"Yahtzee Score\n\nDice Roll: {dice_roll}\n\nScore")
    for scoretype, score in r_dict.items():
        print(f"{scoretype:>20} {score:>5}")
    # print(f"\nTotal: Aces-Sixes = {0}")
    # print("If total score is 63+, then add bonus 35")
    # print(f"Aces-Sixes + Bonus = {0}") # create an extra function to apply bonus points
    # print(f"Yahtzee Bonus Score = {0}")
    # print(f"Total: Lower section = {0}")
    # print(f"\nGrand Total = {0}")

def score_calculator(dice_roll):
    # Scoring Aces - Sixes
    upper_list = [dice_roll.count(i) *i for i in range(1,7)]
    r_dict["Aces"] = upper_list[0]
    r_dict["Twos"] = upper_list[1]
    r_dict["Threes"] = upper_list[2]
    r_dict["Fours"] = upper_list[3]
    r_dict["Fives"] = upper_list[4]
    r_dict["Sixes"] = upper_list[5]
    
    # Scoring lower section
    dice_count = []
    for i in range(1,7):
        dice_count.append(dice_roll.count(i))
    
    dice_set_length = len(set(dice_roll))

    if dice_set_length == 1:
        r_dict["YAHTZEE"] = 50
    elif dice_set_length == 2:
        if 3 in dice_count and 2 in dice_count:
            r_dict["Full House"] = 25
        elif 4 in dice_count:
            kind_four = [4*i for i in range(0,7) if dice_roll.count(i) == 4]
            r_dict["Four of a kind"] = kind_four[0]
    elif 3 in dice_count:
            kind_three = [3*i for i in range(0,7) if dice_roll.count(i) == 3]
            r_dict["Three of a kind"] = kind_three[0]
    elif dice_set_length == 5:
        sorted_set = list(set(dice_roll)).sort()
        if sorted_set == [1, 2, 3, 4, 5] or sorted_set == [2, 3, 4, 5, 6]:
            r_dict["LG Straight"] = 40
        else:
            r_dict["SM Straight"] = 30 # check this one, roll could be 12342, which would be 4 unique numbers, might be better to put the 3 combinations in
    r_dict["Chance"] = sum(dice_roll)

def play_game():
    dice_roll = [random.randrange(1, 7) for i in range(0, 5)]
    score_calculator(dice_roll)
    cl_display(dice_roll)

play_game()
