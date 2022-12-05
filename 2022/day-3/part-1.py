import logging
import sys


logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

with open('input.txt') as f:
    lines = [line for line in f.read().split("\n") if line != ""]


def convert_to_priority(char):
    priority = 0
    value = ord(char)
    if value >= 97:  # lowercase
        priority = value - 96
    else:  # uppercase
        priority = value - 38

    if priority <= 0 or priority > 52:
        raise Exception(f"Failed to parse priority for {char}, got invalid value {priority}")

    return priority


total = 0
for line in lines:

    first = line[:int((len(line) / 2))]
    second = line[int((len(line) / 2)):]

    matching = [item for item in first if item in second][0]
    total += convert_to_priority(matching)

    logging.info(f"{len(line)}: {line}")
    logging.info(f"First : {first}")
    logging.info(f"Second: {second}")
    logging.info(f"Matching: {matching} {convert_to_priority(matching)}")
    logging.info(f"Total: {total}")
    logging.info("-------------------------------")
