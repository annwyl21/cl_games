import sys, random
from datetime import datetime
from games.games import Games, Player

ingame_message_dict = {
    'welcome': ["Welcome to...\n", "Guess\t", "the\t", "Number\t\n\n"],
    'title': "Guess the Number",
    "sorry": "Sorry, I did not understand your choice. \n",
    'end_game_message': "Goodbye"
}

number = random.randint(0,11)
print(number)

def play_game():
    guess = input("I am thinking of a number between 0 and 10\nYou have 5 trys to guess.\nWhat do you think it is?")
    count = 0
    while count != 4:
        count += 1
        if guess == str(number):    
            print(f"Player wins\nCongratulations, you guessed it in {count}.\nMy number was {number}.")
            score_tracker("player")
            break
        elif guess != str(number):
            guess = input("Have another try...")
    save_game()

def score_tracker(winner):
    if winner == "player":
        guess_player.increase_score(1)
    else:
        guess_computer.increase_score(1)

def save_game():
    save = input("Do you wish to save the scores? Y or N")
    if save in ["n", "N", 'q', "Q"]:
        Games.end_game(ingame_message_dict["end_game_message"])
    else:
        now = datetime.now()
        date_time_str = now.strftime("%Y-%m-%d %H:%M")
        with open("saved_score.txt", 'a') as save_score:
            save_score.write(f"{guess_game.get_title():20}  {guess_computer.get_score()}:{guess_player.get_score()}  {date_time_str}\n")
        Games.end_game(ingame_message_dict["end_game_message"])

guess_game = Games('guess')
guess_game.set_title(ingame_message_dict["title"])

guess_game.open_game(ingame_message_dict["welcome"])

guess_computer = Player(0)
guess_player = Player(0)
play_game()
