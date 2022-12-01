import logging
import sys


logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

with open('input.txt') as f:
    lines = f.read()

num = 1
highest = -1
running = 0
for line in lines.split("\n"):

    if not len(line):

        logging.info(f'Elf {num} is carrying {running} calories; highest so far is {highest}')
        if running > highest:
            logging.info(f'Elf {num} is currently carrying the most calories')
            highest = running

        num += 1
        running = 0
        continue

    running += int(line)

logging.info(f'The highest number of calories carried is {highest}')
