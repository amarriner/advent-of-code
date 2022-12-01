import logging
import sys


logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


with open('input.txt') as f:
    lines = f.read()

num = 1
highest = []
running = 0
for line in lines.split("\n"):

    if not len(line):

        highest.append(running)
        highest.sort(reverse=True)
        logging.info(f'Elf {num} is carrying {running} calories; highest three so far are {highest[:3]}')

        num += 1
        running = 0
        continue

    running += int(line)

logging.info(f'The three highest number of calories carried are {highest[:3]}, total: {sum(highest[:3])}')
