import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()
file_handler = logging.FileHandler("day-8-part-2.log", mode="w")
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
    # Calculate scores for each tree
    #
    highest = 0
    for line_index, line in enumerate(lines):

        logging.debug(f" --> line {line_index}")

        #
        # Loop through trees in a line
        #
        for tree_index, tree in enumerate([int(tree) for tree in line]):

            score = 1
            logging.debug(f" ----> tree {tree_index}, line {line_index}, value {tree}")

            #
            # Check in the cardinal directions for shorter trees
            #
            count = 0
            for check in [int(tree) for tree in line[tree_index + 1:]]:
                count += 1
                if check >= tree:
                    break
            if count:
                score = count
            logging.debug(f" ------> [right] can see {count} trees, score: {score}")

            count = 0
            for check in reversed([int(tree) for tree in line[:tree_index]]):
                count += 1
                if check >= tree:
                    break
            if count:
                score *= count
            logging.debug(f" ------> [left] can see {count} trees, score: {score}")

            count = 0
            for row_index in reversed(range(0, line_index)):
                count += 1
                if int(lines[row_index][tree_index]) >= tree:
                    break
            if count:
                score *= count
            logging.debug(f" ------> [up] can see {count} trees, score: {score}")

            count = 0
            for row_index in range(line_index + 1, len(lines)):
                count += 1
                if int(lines[row_index][tree_index]) >= tree:
                    break
            if count:
                score *= count
            logging.debug(f" ------> [down] can see {count} trees, score: {score}")

            #
            # Determine if scenic score is highest
            #
            if score > highest:
                highest = score

    #
    # Results
    #
    logging.info(f"Highest scenic score is: {highest}")
