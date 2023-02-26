# Command Line Games

A selection of command line games in python to demonstrate programming knowledge.

**Rock, Paper, Scissors**

- encapsulated with in a class
- abstracting the scoring system and the count of matches played to be the instance of the class
- scores are saved to a [txt file](./saved_score.txt)
    - Link to [core game code](core_game_rps.py)

## Instructions to play:
**Rock, Paper, Scissors** run:
```bash
python core_game_rps.py
```

Challenges Overcome:
- forgetting to create .gitignore after creating command line repo, and listing my entire venv for commit!
- initially I was tracking the scores in a function but when I revisited the game to encapsulate this in a class, the game code became much clearer to read and easier to edit
- learning the benefits of having version control and a feature branch so my repo always has current, working code on the main branch while I develop on the features branch
