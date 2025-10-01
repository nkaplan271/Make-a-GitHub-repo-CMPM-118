import sys
from rich import print
from time import sleep
import time

def printLines():
    lines = [
        ("I have brought peace................freedom................justice...........and security to my new empire.", 0.06, 1.0),                # pause 1 second after this line
        ("Your new Empire?", 0.05, 1.0), # pause 0.5 seconds
        ("Don't make me kill you.", 0.07, 1.0),                # pause 2 seconds
        ("Anakin...........my allegiance is to the Republic! To Demoncracy!", 0.06, 1.0),
        ("If you're not with me......then you're my enemy.", 0.06, 1.0),
        ("Only a Sith deals in absolutes............I will do what I must.", 0.07, 1.0),
        ("You will try.", 0.06, 1.0),
    ]
    
    for line, char_delay, line_delay in lines:
        for char in line:
            print(char, end='', flush=True)
            sleep(char_delay)
        print()
        sleep(line_delay)  # pause after the whole line

printLines()