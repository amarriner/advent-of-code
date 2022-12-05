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
for i in range(0, len(lines), 3):

    group1 = lines[i]
    group2 = lines[i + 1]
    group3 = lines[i + 2]

    matching = [item for item in group1 if item in group2 and item in group3][0]
    total += convert_to_priority(matching)

    logging.info(f"Group 1: {group1}")
    logging.info(f"Group 2: {group2}")
    logging.info(f"Group 3: {group3}")
    logging.info(f"Matching: {matching} {convert_to_priority(matching)}")
    logging.info(f"Total: {total}")
    logging.info("-------------------------------")
