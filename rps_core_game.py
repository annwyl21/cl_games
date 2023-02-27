import random, time, sys
from datetime import datetime

ingame_message_dict = {
    "computer": "\tComputer is the WINNER\t\n", 
    "Rock": ">>>>> Rock smashes Scissors <<<<<\n", 
    "Paper": ">>>>> Paper wraps Rock <<<<<\n", 
    "Scissors": ">>>>> Scissors cut Paper <<<<<\n", 
    "player": "Congratulations you are the winner!", 
    "draw": "\t<<<<< DRAW >>>>>\t\n", 
    "get_ready": [" Ready    ", "Set   ", "Go\n"], 
    'welcome': ["Welcome to...\n", "Rock\t", "Paper\t", "Scissors\t\n\n"],
    "sorry": "Sorry, I did not understand your choice. \n",
                       }

# ABSTRACTION - the object here is the score and match count that I need to track through the game for both player and computer and not the game title etc
# ENCAPSULATION - the score tracker is encapsulated here so it is not dragged through functions and over complicating the game code

class Game_rps:

    def __init__(self, player_score=0, computer_score=0, match_count=0):
        self._player_score = player_score
        self._computer_score = computer_score
        self._match_count = match_count
    
    def increase_score(self, winner):
        if winner == "player":
            self._player_score += 1
        else:
            self._computer_score += 1
    
    # getter DATA
    def get_player_score(self):
        return self._player_score
    
    # getter DATA
    def get_computer_score(self):
        return self._computer_score
    
    def increase_match_count(self):
        self._match_count += 1
    
    # getter DATA
    def get_match_count(self):
        return self._match_count
    
    def set_winner(self, winner):
        self._winner = winner

    def get_winner(self):
        return self._winner
    
    def end_game(self):
        print("Goodbye\n", "="*50)
        sys.exit()
    
    def validate(self, data_to_check):
        self.data_to_check = data_to_check.upper()
        user_dict = {"R": "Rock", "P": "Paper", "S": "Scissors"}
        if self.data_to_check in user_dict.keys():
            return user_dict[self.data_to_check]
        else:
            while self.data_to_check not in user_dict.keys():
                if self.data_to_check == "Q" or self.data_to_check == "q":
                    self.save_game()
                else:
                    print(ingame_message_dict["sorry"])
                    self.data_to_check = input("\n\t(R)ock\n\t(P)aper\n\t(S)cissors\n\t(Q)uit\n")

    def game_logic(self, computer_choice, user_choice):
        if user_choice == computer_choice:
            print(ingame_message_dict["draw"])
        # winning scenarios for computer
        elif (user_choice == "Rock" and computer_choice == "Paper") or (user_choice == "Paper" and computer_choice == "Scissors") or (user_choice == "Scissors" and computer_choice == "Rock"):
            self.set_winner("computer")
            self.result_message(computer_choice)
            self.increase_score("computer")
        else:
            self.set_winner("player")
            self.result_message(user_choice)
            self.increase_score("player")
    
    def result_message(self, choice):
        print(ingame_message_dict[choice])
        if self.get_winner() == "computer":
            ingame_message_dict[self.get_winner()]
        else:
            winner_message = ingame_message_dict[self.get_winner()]
            print("*" * 6 + "*" * len(winner_message) + "*" * 6)
            print("*" * 6 + winner_message + "*" * 6)
            print("*" * 6 + "*" * len(winner_message) + "*" * 6)
            print()

    def save_game(self):
        save = input("Do you wish to save the scores? Y or N ")
        if save in ["n", "N", 'q', "Q"]:
            self.end_game()
        else:
            now = datetime.now()
            date_time_str = now.strftime("%Y-%m-%d %H:%M")
            with open("saved_score.txt", 'a') as save_score:
                save_score.write(f"Rock, Paper, Scissors  {self.get_computer_score()}:{self.get_player_score()}  {date_time_str}\n")
            self.end_game()

    def play_game(self):

        # use the jazzy game opening and progress bar on the first match only
        if self.get_match_count() == 0:
            for item in ingame_message_dict['welcome']:
                time.sleep(0.85)
                print(item, end = '', flush = True)
            print("Lets choose now\nI am thinking")
            for _ in range(26):
                time.sleep(0.15)
                print('.', end = '', flush=True)
        
        # making rock, paper, scissors choices
        computer_choice = random.choice(["Rock", "Paper", "Scissors"])
        data_to_check = input("\n\t(R)ock\n\t(P)aper\n\t(S)cissors\n\t(Q)uit\n")
        user_choice = self.validate(data_to_check)
        print(f"\tYou chose {user_choice}\n\tand\t\n\tComputer chose {computer_choice}\n")

        # calling game logic
        self.game_logic(computer_choice, user_choice)
    
        # end of match, print score and count matches
        self.increase_match_count()
        print(f"Your score is {self.get_player_score()} and the computer has {self.get_computer_score()}.\nGames played {self.get_match_count()}")
        
        # play again
        decision = input("Press enter to play again or Q to quit\n")  # Q is hardcoded so this text is not available to modify in the game dictionary
        if decision in ["Q", "q"]:
            self.save_game()
        else:
            self.play_game()

rpsgame = Game_rps() # create instance of the game passing in arguments to set the player score, computer score and count of matches played

if __name__ == "__main__":
    rpsgame.play_game() # call a method on the instance of the game to start play
