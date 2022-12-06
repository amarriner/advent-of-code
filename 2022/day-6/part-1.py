import logging
import sys


logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

MARKER_SIZE = 4

with open('input.txt') as f:

    buffer = f.read()

for index, char in enumerate(buffer[:len(buffer) - MARKER_SIZE]):
    marker = buffer[index:index + MARKER_SIZE]
    if len(set(marker)) == MARKER_SIZE:
        logging.info(f'Found marker {marker} at index {index}, needed to process {index + MARKER_SIZE} characters first')
        break
