import logging
import re
import sys


logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

STACK_WIDTH = 4
STACK_PATTERN = re.compile(r'[A-Z]')
INSTRUCTION_PATTERN = re.compile(r'^move ([0-9]+) from ([0-9]+) to ([0-9]+)$')

#
# Parse input
#
with open('input.txt') as f:

    stacks, instructions = f.read().split("\n\n")

    num_stacks = int(stacks.split("\n")[-1].split()[-1])
    input_stacks = [stack for stack in stacks.split("\n")[:-1] if stack != ""]
    instructions = [instruction for instruction in instructions.split("\n") if instruction != ""]

#
# Generate stacks from input
#
stacks = []
for i in range(0, num_stacks):
    stacks.append([])

for index, stack in enumerate(input_stacks):

    for i in range(0, num_stacks):

        start = STACK_WIDTH * i

        if STACK_PATTERN.match(stack[start + 1:start + 2]):
            stacks[i].append(stack[start + 1:start + 2])

for i in range(0, num_stacks):
    logging.info(stacks[i])

#
# Process instructions
#
for instruction in instructions:

    num, from_, to = [int(value) for value in INSTRUCTION_PATTERN.search(instruction).groups()]
    logging.info(f'Moving {num} crates from stack {from_} to stack {to}')
    from_ -= 1
    to -= 1

    temp_list = []
    for i in range(0, num):
        temp_list.append(stacks[from_].pop(0))

    stacks[to] = temp_list + stacks[to]

#
# Results
#
logging.info('-----------------------------------------------------------------')
for i in range(0, num_stacks):
    logging.info(stacks[i])

logging.info("".join([stack[0] for stack in stacks]))
