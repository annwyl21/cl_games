import pytest
from rps_core_game import *

# DON'T FORGET TO TYPE PYTEST INSTEAD OF PYTHON

# # Example from webpage
# def func(x):
#     return x + 1
# def test_answer():
#     assert func(3) == 5

# my logic copied from the game to this file
# def game_logic(computer_choice, user_choice):
#     winner = ""
#     if user_choice == computer_choice:
#         # print(ingame_message_dict["draw"])
#         winner = "None"
#     # winning scenarios for computer
#     elif (user_choice == "Rock" and computer_choice == "Paper") or (user_choice == "Paper" and computer_choice == "Scissors") or (user_choice == "Scissors" and computer_choice == "Rock"):
#         winner = "computer"
#         # self.result_message(computer_choice)
#         # self.increase_score("computer")
#     else:
#         winner = "player"
#         # self.result_message(user_choice)
#         # self.increase_score("player")
#     # self.set_winner(winner)
#     return winner


# PYTEST - checking the function within the game
# tests 1 thing
def test_check_game_logic():
    results = Game_rps().game_logic(computer_choice = "Rock", player_choice = "Paper")
    assert results == "player", "wrong result"

# tests all of the possible scenarios
@pytest.mark.parametrize("computer_choice, player_choice, answer", [
        ("Rock", "Rock", "draw"),
        ("Rock", "Paper", "player"),
        ("Rock", "Scissors", "computer"),
        ("Scissors", "Scissors", "draw"),
        ("Scissors", "Rock", "player"),
        ("Scissors", "Paper", "computer"),
        ("Paper", "Paper", "draw"),
        ("Paper", "Rock", "computer"),
        ("Paper", "Scissors", "player")
    ])
def test_test_game_logic(computer_choice, player_choice, answer):
    results = Game_rps().game_logic(computer_choice, player_choice)
    assert results == answer, "wrong result"
