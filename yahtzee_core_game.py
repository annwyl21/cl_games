import random
from yahtzee_player import Yahtzee_player

# ABSTRACTION: Each game is a series of updated dictionaries
# ENCAPSULATION: Each game instance is a cycle through of updated dictionaries returning an overall result after 13 cycles

class Game_Yahtzee:

    def computer_turn(player):
        if player == "computer":
            score = Yahtzee_player("computer", [])



    # def player_turn():
    #                     dice_roll = []
    #             for _ in range (5):
    #                 number = input("Enter a dice number and press enter")
    #                 dice_roll.append(number)
    #             print(f"You entered {dice_roll}, let\'s see how that scores")
    #             player = Yahtzee_player(player, dice_roll).calculate_score()

    def determine_winner():
        pass

    def play_game():

        #determine players
        print("Yahtzee\n")
        print("You can play against the computer.\n You need 5 dice.")
        player_name = input("Enter your name")
        players = ["computer"]
        players.insert(1, player_name)

        # create player instance
        for player in players:
            player = Yahtzee_player(player, [])   
        
        # play 13 turns
        for _ in range(13):
            for player in players:
                print(f"It is {player}\'s turn.")
                player = Yahtzee_player(player, []).calculate_score()
                self.player_turn(player)
        
        self.determine_winner()

    # def take_turn(self):
    #     self.player_name = Yahtzee_turn("computer", []).calculate_score()

    # def update_game_status(self):


# def cl_display(dice_roll, r_dict):
#     print(f"Yahtzee Score\n\nDice Roll: {dice_roll}\n\nScore")
#     for scoretype, score in r_dict.items():
#         print(f"{scoretype:>20} {score:>5}")
#     # print(f"\nTotal: Aces-Sixes = {0}")
#     # print("If total score is 63+, then add bonus 35")
#     # print(f"Aces-Sixes + Bonus = {0}") # create an extra function to apply bonus points
#     # print(f"Yahtzee Bonus Score = {0}")
#     # print(f"Total: Lower section = {0}")
#     # print(f"\nGrand Total = {0}")

#     apply bonuses function

# call score caluclator

# def play_game():
#     dice_roll = [random.randrange(1, 7) for i in range(0, 5)]
#     results_dict = Yahtzee_calc.calculator(dice_roll)
#     cl_display(dice_roll, results_dict)

if __name__ == "__main__":
    Game_Yahtzee().play_game()
