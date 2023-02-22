import secrets, time, sys
import score

ingame_message_dict = {"winner_c": "\tComputer is the WINNER\t\n", "rock_win": ">>>>> Rock smashes Scissors<<<<<\n", "paper_win": ">>>>> Paper wraps Rock<<<<<\n", "scissors_win": ">>>>> Scissors cut Paper<<<<<\n", "winner_u": "Congratulations you are the winner!", "draw": "\tIt was a draw\t\n", "get_ready": [" Ready    ", "Set   ", "Go\n"], 'welcome': ["Welcome to...\n","Rock\t", "Paper\t", "Scissors\t\n\n"], "sorry": "Sorry, I did not understand your choice. \n"}

def make_choice(**who_what):  # using **kwargs which takes the arguments and puts them in an invisible dictionary
    if who_what['selector'] == "Computer":  # accessing the keyword argument using a dictionary key
        return secrets.choice(["Rock", "Paper", "Scissors"])
    elif who_what['selector'] == "Player":
        user_dict = {"R": "Rock", "P": "Paper", "S": "Scissors"}
        data_to_check = who_what["data"].upper()
        if data_to_check == "Q":
            end_game()
        elif data_to_check in ["R", "P", "S"]:
        # elif data_to_check == "R" or data_to_check == "S" or data_to_check == "P":
            if data_to_check in user_dict:
                return user_dict[data_to_check]
        else:
            print(ingame_message_dict["sorry"])
            play_again(who_what["player_score"], who_what["computer_score"])      

def play_game(player_score, computer_score):
    score.thinking()
    computer = make_choice(selector = "Computer")
    human_input = input("\n\tR = Rock\n\tP = Paper\n\tS = Scissors\n\tQ = Quit\nPlease enter R, P, S or Q:\n")
    user = make_choice(selector = "Player", data = human_input, player_score = player_score, computer_score = computer_score)
    print(f"\tYou chose {user}\n\tand\t\n\tComputer chose {computer}\n")
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
            congratulations()
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
    score_tuple = score.score_tracker(winner, player_score, computer_score)
    new_player_score, new_computer_score = score_tuple #unpacking a tuple
    play_again(new_player_score, new_computer_score)

def congratulations():
    winner_message = ingame_message_dict["winner_u"]
    print("*" * 6 + "*" * len(winner_message) + "*" * 6)
    print("*" * 6 + winner_message + "*" * 6)
    print("*" * 6 + "*" * len(winner_message) + "*" * 6)
    print()

def end_game():
    print("Goodbye\n", "="*50)
    sys.exit()

def play_again(player_score, computer_score):
    decision = input("Press enter to play again or Q to quit\n")  # Q is hardcoded so this text is not available to modify in the game dictionary
    if decision in ["Q", "q"]:
    #if decision == "Q" or decision == "q":
        end_game()
    else:
        play_game(player_score, computer_score)

def open_game():
    for item in ingame_message_dict['welcome']:
        time.sleep(0.85)
        print(item, end = '', flush = True)
    play_game(player_score = 0, computer_score = 0)
    
open_game()
