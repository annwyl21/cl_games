# Command Line Games

A selection of command line games in python to demonstrate programming knowledge, built around a [Games class](./games/games.py).

**Rock, Paper, Scissors**

- A small command line game that has multiple functions linking across 2 files, using imported modules (sys, time) and features from 2 classes; Games & Players.
- The game also offers tha player the option to save the end score to a file. 
- The game has an in-game message dictionary that is separate from the code where game messages can be edited without needing to trawl through the code. 
- The code also demonstrates my programming knowledge of **kwargs, tuple unpacking and positionally based arguments in function parameters.
    - Link to [core game code](core_game_rps.py)
    - Link to [RPS Feature Details](README_rps.md)

## Instructions to play:
**Rock, Paper, Scissors** run:
```bash
python core_game_rps.py
```

Challenges Overcome:
- forgetting to create .gitignore after creating command line repo, and listing my entire venv for commit!
- editing the scoring system from a function on another page that was tracking the scores as parameters through all the other functions called, into a Player class that tracks the scores independently was a challenge... but also demonstrated the real benefits of using classes to simplify my code
- learning the benefits of having version control and a feature branch so my repo always has current, working code on the main branch while I develop on the features branch

