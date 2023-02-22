import random

def dice_dictionary():
    dice_roll = [random.randrange(1, 7) for i in range(0, 5)]
    dice_roll_dictionary = {}
    for i in range(1,7):
        dice_roll_dictionary[i] = dice_roll.count(i)
    return dice_roll, dice_roll_dictionary

def upper_section(dice_roll):
    list_to_sum = [dice_roll.count(i) *i for i in range(1,7)] # could this be a lambda function?
    return sum(list_to_sum)

def lower_section(dice_roll, game_dictionary):
    dice_set_length = len(set(dice_roll))
    dice_count = []
    for i in range(1,7):
        dice_count.append(dice_roll.count(i))
    print(dice_count)
    results_dictionary = {"Three of a kind": 0, "Four of a kind": 0, "Full House": 0, "SM Straight": 0, "LG Straight": 0, "YAHTZEE": 0}
    if dice_set_length == 1:
        results_dictionary["YAHTZEE"] = 50
    elif dice_set_length == 2:
        if 3 in dice_count and 2 in dice_count:
            results_dictionary["Full House"] = 25
        elif 4 in dice_count:
            kind_four = [4*i for i in range(0,7) if dice_roll.count(i) == 4]
            results_dictionary["Four of a kind"] = kind_four[0]
    elif 3 in dice_count:
            kind_three = [3*i for i in range(0,7) if dice_roll.count(i) == 3]
            results_dictionary["Three of a kind"] = kind_three[0]
    elif dice_set_length == 5:
        #results_dictionary["LG Straight"] = 40
#either a sequence of 4 or a sequence of 5
    # Sequence of Four
    #sequence_of_four = 0
    #score 30
        pass
    return results_dictionary

def cl_display(dice_roll, game_dictionary, result_upper, results_dictionary):
    print("Yahtzee Score:")
    print("Dice Roll:", dice_roll)
    print("Score for upper section:", result_upper)
    result_lower = 0
    for score in results_dictionary.values():
        result_lower += score
    print("Score for lower section:", result_lower)
    print(results_dictionary)

def play_game():
    game_tuple = dice_dictionary()
    dice_roll, game_dictionary = game_tuple
    result_upper = upper_section(dice_roll)
    result_lower = lower_section(dice_roll, game_dictionary)
    cl_display(dice_roll, game_dictionary, result_upper, result_lower)

play_game()
