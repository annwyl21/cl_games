import pytest
import rps_core_game

# DON'T FORGET TO TYPE PYTEST INSTEAD OF PYTHON

# # Example from webpage
# def func(x):
#     return x + 1

# def test_answer():
#     assert func(3) == 5

def game_logic(computer_choice, user_choice):
    winner = ""
    if user_choice == computer_choice:
        # print(ingame_message_dict["draw"])
        winner = "None"
    # winning scenarios for computer
    elif (user_choice == "Rock" and computer_choice == "Paper") or (user_choice == "Paper" and computer_choice == "Scissors") or (user_choice == "Scissors" and computer_choice == "Rock"):
        winner = "computer"
        # self.result_message(computer_choice)
        # self.increase_score("computer")
    else:
        winner = "player"
        # self.result_message(user_choice)
        # self.increase_score("player")
    # self.set_winner(winner)
    return winner



def check_game_logic():
    computer_choice = "Rock"
    user_choice = "Paper"
    results = game_logic(computer_choice, user_choice)
    assert results == "None"

