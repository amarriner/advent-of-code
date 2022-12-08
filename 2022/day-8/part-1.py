import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()
file_handler = logging.FileHandler("day-8-part-1.log", mode="w")
logger.addHandler(file_handler)
logger.handlers = [handler for handler in logger.handlers if not type(handler) == logging.StreamHandler]


if __name__ == '__main__':

    #
    # Read input trees
    #
    with open('input.txt') as f:
        lines = [line for line in f.read().split("\n") if line != ""]
        logging.info(f"Read in {len(lines)} of trees with {len(lines[0])} trees per line")

    #
    # Look for visible trees
    #
    visible = 0
    for line_index, line in enumerate(lines):

        logging.debug(f" --> line {line_index}")

        #
        # If we're on the first or last line, all trees are visible
        #
        if line_index in [0, len(line) - 1]:
            visible += len(line)
            continue

        #
        # Loop through trees in a line
        #
        for tree_index, tree in enumerate([int(tree) for tree in line]):

            logging.debug(f" ----> tree {tree_index}")

            #
            # If we're at the first tree or last tree in a line, they're visible
            #
            if tree_index in [0, len(line) - 1]:
                visible += 1
                continue

            #
            # Check in the cardinal directions
            #
            count = 0
            for check_index, check in enumerate([int(tree) for tree in line[tree_index + 1:]]):
                if check >= tree:
                    logging.debug(f" ------> [forward] Tree {check_index} in the same row {line_index} is taller {check} than the current tree {tree}, index {tree_index}")
                    count += 1
                    break
            for check_index, check in enumerate([int(tree) for tree in line[:tree_index]]):
                if check >= tree:
                    logging.debug(f" ------> [backward] Tree {check_index} in the same row {line_index} is taller {check} than the current tree {tree}, index {tree_index}")
                    count += 1
                    break
            for row_index in range(0, line_index):
                if int(lines[row_index][tree_index]) >= tree:
                    logging.debug(f" ------> [up] Tree {tree_index} in row {row_index} is taller {int(lines[row_index][tree_index])} than the current tree {tree}, index {tree_index}")
                    count += 1
                    break
            for row_index in range(line_index + 1, len(lines)):
                if int(lines[row_index][tree_index]) >= tree:
                    logging.debug(f" ------> [down] Tree {tree_index} in row {row_index} is taller {int(lines[row_index][tree_index])} than the current tree {tree}, index {tree_index}")
                    count += 1
                    break

            #
            # If we're blocked in all four directions, the tree is not visible
            #
            if count != 4:
                visible += 1

    #
    # Results
    #
    logging.info(f"Total trees visible: {visible}")
