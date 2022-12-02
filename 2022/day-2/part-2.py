import logging
import sys


logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

with open('input.txt') as f:
    lines = [line for line in f.read().split("\n") if line != ""]


outcomes = {
    'AX': 3,  # rock lose
    'AY': 4,  # rock draw
    'AZ': 8,  # rock win

    'BX': 1,  # paper lose
    'BY': 5,  # paper draw
    'BZ': 9,  # paper win

    'CX': 2,  # scissors lose
    'CY': 6,  # scissors draw
    'CZ': 7   # scissors win
}

score = 0
for opponent, me in [(item.split(" ")[0], item.split(" ")[1]) for item in lines]:
    logging.info(f'{opponent} {me} = {outcomes[opponent + me]}')
    score += outcomes[opponent + me]

logging.info(f"Final score is: {score}")
