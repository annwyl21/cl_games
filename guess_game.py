import sys, random
from datetime import datetime
from games.games import Games, Player

ingame_message_dict = {
    "get_ready": [" Ready    ", "Set   ", "Go\n"], 
    'welcome': ["Welcome to...\n", "Guess\t", "the\t", "Number\t\n\n"],
    'title': "Guess the Number",
    "sorry": "Sorry, I did not understand your choice. \n",
    'end_game_message': "Goodbye"
}

def play_game():
    number = random.randint(0,11)
    guess = input("I am thinking of a number between 0 and 10\nYou have 5 trys to guess.\nWhat do you think it is?")
    count = 1
    
    while count < 6:
        if guess != number:
            play_game()
        else:    
            print("Congratulations, you guessed it in {count}.\nMy number was {number}.")
    


guess_game = Games('guess')
guess_game.set_title(ingame_message_dict["title"])

guess_game.open_game(ingame_message_dict["welcome"])

guess_computer = Player(0)
guess_player = Player(0)
play_game()