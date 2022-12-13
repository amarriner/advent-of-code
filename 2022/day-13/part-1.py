import ast
import logging


# -----------------------------------------------------------------------------
# INIT
# -----------------------------------------------------------------------------
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()
file_handler = logging.FileHandler("day-13-part-1.log", mode="w")
logger.addHandler(file_handler)
# logger.handlers = [handler for handler in logger.handlers if not type(handler) == logging.StreamHandler]


# -----------------------------------------------------------------------------
# HELPERS
# -----------------------------------------------------------------------------
def process_pair(left, right):

    logging.debug("=========================================")
    logging.debug(f"Processing left {left} and right {right}")

    if type(left) == int and type(right) == int:
        if left < right:
            logging.debug(" [I]: True")
            return True
        elif left > right:
            logging.debug(" [I]: False")
            return False
        else:
            logging.debug(" [I]: None")
            return None

    elif type(left) == int and type(right) == list:
        logging.debug(" [C]: left")
        return process_pair([left], right)
    elif type(left) == list and type(right) == int:
        logging.debug(" [C]: right")
        return process_pair(left, [right])

    elif type(left) == list and type(right) == list:

        for index, value in enumerate(left):

            if index < len(right):
                result = process_pair(left[index], right[index])
                if result is None:
                    continue
                logging.debug(f" [I]: {result}")
                return result

        if len(left) < len(right):
            logging.debug(" [L]: True")
            return True
        elif len(left) > len(right):
            logging.debug(" [L]: False")
            return False
        else:
            logging.debug(" [L]: None")
            return None

    raise Exception(f"Failed to process pair, {left} and {right}")


# -----------------------------------------------------------------------------
# MAIN
# -----------------------------------------------------------------------------
if __name__ == '__main__':

    with open('input.txt') as f:
        pairs = []
        for pair in f.read().split("\n\n"):
            pairs.append([ast.literal_eval(item) for item in pair.split("\n")[:2]])

    logging.debug(pairs)

    indices = []
    for index, pair in enumerate(pairs):
        if process_pair(*pair) is True:
            indices.append(index + 1)

    # -------------------------------------------------------------------------
    # RESULTS
    # -------------------------------------------------------------------------
    logging.info('-------------------------------------------------------------')
    logging.info(f"Indices: {indices}, sum: {sum(indices)}")
