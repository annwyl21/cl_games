# Rock, Paper, Scissors

My game has 6 functions that I wrote on the game page:
 - open_game() uses the sleep module to make the loading deliberately slower and build excitement and anticipation,
       separated from play_game() so the user is not subsequently bored by this intro if they choose to play again
 - play_game() this is the core of the game, it has a nice start and contains all of the conditional logic
 - make_choice() this is called twice; first to generate a random choice from a list that represents the computers 'choice' and second to decode the user input
       it can take multiple named keyword arguments; the player (computer or human) and the user choice input and scores to track
       mostly here so I can play with **kwargs to be honest, it could have been part of the core play_game()
 - congratulations() this function is called when the user wins
 - play_again() this function allows the user to choose to continue play without having to reload the game, or choose to quit and end the program, it also tracks the score
 - end_game() this function closes the program

 My solution also uses 3 imported modules and 1 imported function:
 - secrets - used to generate a crytographically strong random choice from a list of 3 that represents the computers choice
 - time - used to add a jazzy opening on to my game
 - sys - used to end the game
 - score_tracker() - an imported function that takes 3 arguments, updates the score and returns a tuple that is refered into the play_again function to track the ongoing score

 My solution uses a game message dictionary that is global in scope
       so that game play text can be modified in 1 place
       The game message dictionary does not include any text that refers to instructions that are hard-coded such as the letters typed to indicate a user-choice
 There are also 2 dictionaries that are local in scope, where availability is limited to within the function; 
       these dictionary holds the data to decode the user and computer choices
 There is also an invisible dictionary holding the keyword arguments sent in (**kwargs) used in the parameters of the make-choice function