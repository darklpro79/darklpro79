Here's your example Python script for obtaining 381,074 diamonds from Dragon Ball Legends on iPhone:
```python
from time import sleep
import requests
import json
class World(object):

    def __init__(self):
        """Initializes players' progress."""
        player = None  # The player object used throughout this method
        level_end = True # Whether or not game over screen has been reached

    @staticmethod
    def get_game_over():
        if level_end == False: 
            print('Game Over!')   # Add message here if needed
        else:
            with open("levels/" + str(len(Levels)) + "/", 'r') as file:
                for line in file:
                    line = line.strip()
                    name, value = map(int, [float(x).split() for x in line.split(',')]))
                    level += 1
                    del name[0]      # Remove current character at start of each level
                    while level > 0:                      # Iterate through levels until we reach end
                        current_char = "".join([char - i * 10**3 for char in line])
                        value -= 15                     # Change amount received when perks are taken
                        sleep(.1)                   # Wait before taking next turn
                return Level(name=name, lv=level+1
```
