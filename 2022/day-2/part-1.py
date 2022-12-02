import logging
import sys


logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

with open('input.txt') as f:
    lines = [line for line in f.read().split("\n") if line != ""]


outcomes = {
    'AX': 4,  # rock rock
    'AY': 8,  # rock paper
    'AZ': 3,  # rock scissors

    'BX': 1,  # paper rock
    'BY': 5,  # paper paper
    'BZ': 9,  # paper scissors

    'CX': 7,  # scissors rock
    'CY': 2,  # scissors paper
    'CZ': 6   # scissors scissors
}

score = 0
for opponent, me in [(item.split(" ")[0], item.split(" ")[1]) for item in lines]:
    logging.info(f'{opponent} {me} = {outcomes[opponent + me]}')
    score += outcomes[opponent + me]

logging.info(f"Final score is: {score}")
