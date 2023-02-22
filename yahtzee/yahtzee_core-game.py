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
    kind_three = [3*i for i in range(0,7) if dice_roll.count(i) == 3]
    kind_four = [4*i for i in range(0,7) if dice_roll.count(i) == 4]
    full_house = 0
    sequence_of_four = 0
    sequence_of_five = 0
    for i in range(0,7):
        if dice_roll.count(i) == 3:
            pass
    return kind_three, kind_four, full_house, sequence_of_four, sequence_of_five

def cl_display(dice_roll, game_dictionary, result_upper, result_lower):
    print(f"A nice CL display of results {dice_roll}{game_dictionary}{result_upper}{result_lower}")

def play_game():
    game_tuple = dice_dictionary()
    dice_roll, game_dictionary = game_tuple
    result_upper = upper_section(dice_roll)
    result_lower = lower_section(dice_roll, game_dictionary)
    cl_display(dice_roll, game_dictionary, result_upper, result_lower)

play_game()
