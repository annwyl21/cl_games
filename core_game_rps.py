import random, time, sys
from datetime import datetime

ingame_message_dict = {
    "winner_c": "\tComputer is the WINNER\t\n", 
    "rock_win": ">>>>> Rock smashes Scissors<<<<<\n", 
    "paper_win": ">>>>> Paper wraps Rock<<<<<\n", 
    "scissors_win": ">>>>> Scissors cut Paper<<<<<\n", 
    "winner_u": "Congratulations you are the winner!", 
    "draw": "\t<<<<< DRAW >>>>>\t\n", 
    "get_ready": [" Ready    ", "Set   ", "Go\n"], 
    'welcome': ["Welcome to...\n", "Rock\t", "Paper\t", "Scissors\t\n\n"],
    "sorry": "Sorry, I did not understand your choice. \n",
    'end_game_message': "Goodbye"
                       }

# ABSTRACTION - the object here is the score that I need to track through the game for both player and computer and not the game title etc
# ENCAPSULATION - the score tracker is encapsulated here so it is not dragged through functions and over complicating the game

class Game_rps:

    def __init__(self, opening_score):
        self._score = opening_score

    # BEHAVIOUR
    def increase_score(self):
        self._score += 1
    
    # getter DATA
    def get_score(self):
        return self._score
    
    def end_game():
        print("Goodbye\n", "="*50)
        sys.exit()
    
    def validate(self, data_to_check):
        self.data_to_check = data_to_check
        user_dict = {"R": "Rock", "P": "Paper", "S": "Scissors"}
        while data_to_check.upper() not in user_dict.keys():
            if data_to_check == "Q":
                Game_rps.save_game()
            else:
                print(ingame_message_dict["sorry"])
                data_to_check = input("\n\t(R)ock\n\t(P)aper\n\t(S)cissors\n\t(Q)uit\n")
        return user_dict[data_to_check]
    
    def congratulations():
        winner_message = ingame_message_dict["winner_u"]
        print("*" * 6 + "*" * len(winner_message) + "*" * 6)
        print("*" * 6 + winner_message + "*" * 6)
        print("*" * 6 + "*" * len(winner_message) + "*" * 6)
        print()

    def save_game():
        save = input("Do you wish to save the scores? Y or N")
        if save in ["n", "N", 'q', "Q"]:
            Game_rps.end_game(ingame_message_dict["end_game_message"])
        else:
            now = datetime.now()
            date_time_str = now.strftime("%Y-%m-%d %H:%M")
            with open("saved_score.txt", 'a') as save_score:
                save_score.write(f"Rock, Paper, Scissors  {rps_computer.get_score()}:{rps_player.get_score()}  {date_time_str}\n")
            Game_rps.end_game(ingame_message_dict["end_game_message"])


    def play_game():

        # jazzy game opening
        for item in ingame_message_dict['welcome']:
            time.sleep(0.85)
            print(item, end = '', flush = True)
    
        # progress bar to appear as if the computer is "thinking"
        print("Lets choose now\nI am thinking")
        for i in range(26):
            time.sleep(0.15)
            print('.', end = '', flush=True)

        # create choices
        computer = random.choice(["Rock", "Paper", "Scissors"])
        data_to_check = input("\n\t(R)ock\n\t(P)aper\n\t(S)cissors\n\t(Q)uit\n")
        user = self.validate(data_to_check)
        print(f"\tYou chose {user}\n\tand\t\n\tComputer chose {computer}\n")
    
        #game logic
        winner = ""
        if user == computer:
            print(ingame_message_dict["draw"])
            winner = "None"
        elif user == "Rock":
            if computer == "Paper":
                print(ingame_message_dict["paper_win"], ingame_message_dict["winner_c"])
                winner = "computer"
            else:
                print(ingame_message_dict["rock_win"])
                self.congratulations()
                winner = "player"
        elif user == "Paper":
            if computer == "Scissors":
                print(ingame_message_dict["scissors_win"], ingame_message_dict["winner_c"])
                winner = "computer"
            else:
                print(ingame_message_dict["paper_win"])
                congratulations()
                winner = "player"
        else:  # if the human_player chooses Scissors
            if computer == "Rock":
                print(ingame_message_dict["rock_win"], ingame_message_dict["winner_c"])
                winner = "computer"
            else:
                print(ingame_message_dict["scissors_win"])
                congratulations()
                winner = "player"

        #scoring
        if winner == "computer":
            rps_computer.increase_score(1)
        else:
            rps_player.increase_score(1)
        print(f"Your score is {rps_player.get_score()} and the computer has {rps_computer.get_score()}.")

        # play again
        decision = input("Press enter to play again or Q to quit\n")  # Q is hardcoded so this text is not available to modify in the game dictionary
        if decision in ["Q", "q"]:
            Game_rps.save_game()
        else:
            Game_rps.play_game()

rps_computer = Game_rps(0)
rps_player = Game_rps(0)
Game_rps.play_game()
