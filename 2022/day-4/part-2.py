import logging
import sys

from collections import namedtuple


logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


with open('input.txt') as f:
    lines = [line for line in f.read().split("\n") if line != ""]

total = 0
Elf = namedtuple('Elf', 'min max')
for index, line in enumerate(lines):

    elf1, elf2 = [Elf(*[int(num) for num in item.split("-")]) for item in line.split(",")]

    if len([item for item in range(elf1.min, elf1.max + 1) if item in range(elf2.min, elf2.max + 1)]):
        total += 1
    elif len([item for item in range(elf2.min, elf2.max + 1) if item in range(elf1.min, elf1.max + 1)]):
        total += 1

    logging.info(f"Elf 1: {elf1}")
    logging.info(f"Elf 2: {elf2}")
    logging.info(f"[{index}] Total: {total}")
    logging.info("------------------------------------")
