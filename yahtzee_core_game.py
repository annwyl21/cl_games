import random


def cl_display(dice_roll, r_dict):
    print(f"Yahtzee Score\n\nDice Roll: {dice_roll}\n\nScore")
    for scoretype, score in r_dict.items():
        print(f"{scoretype:>20} {score:>5}")
    # print(f"\nTotal: Aces-Sixes = {0}")
    # print("If total score is 63+, then add bonus 35")
    # print(f"Aces-Sixes + Bonus = {0}") # create an extra function to apply bonus points
    # print(f"Yahtzee Bonus Score = {0}")
    # print(f"Total: Lower section = {0}")
    # print(f"\nGrand Total = {0}")

    apply bonuses function

call score caluclator

def play_game():
    dice_roll = [random.randrange(1, 7) for i in range(0, 5)]
    results_dict = score_calculator(dice_roll)
    cl_display(dice_roll, results_dict)

if __name__ == "__main__":
    play_game()
