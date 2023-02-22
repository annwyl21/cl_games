import random

dice_roll = [random.randrange(1, 7) for i in range(0, 5)]

def upper_section(dice_roll):
    list_to_sum = [dice_roll.count(i) *i for i in range(1,7)] # could this be a lambda function?
    return sum(list_to_sum)
    
print(upper_section(dice_roll))

def lower_section(dice_roll):
    pass