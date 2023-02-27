import pytest
import rps_core_game

def check_game_logic():
    computer_choice = "Rock"
    user_choice = "Paper"
    results = rps_core_game.rpsgame.game_logic(computer_choice, user_choice)
    assert results == "None", "broken"

