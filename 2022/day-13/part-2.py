import ast
import logging
import math


# -----------------------------------------------------------------------------
# INIT
# -----------------------------------------------------------------------------
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()
file_handler = logging.FileHandler("day-13-part-2.log", mode="w")
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


def bubble_sort(array):

    swapped = True
    length = len(array)

    while swapped:

        swapped = False

        for i in range(1, length):

            if process_pair(array[i], array[i - 1]) is True:
                temp = array[i - 1]
                array[i - 1] = array[i]
                array[i] = temp
                swapped = True

        length -= 1

    return array


# -----------------------------------------------------------------------------
# MAIN
# -----------------------------------------------------------------------------
if __name__ == '__main__':

    dividers = [[[2]], [[6]]]

    with open('input.txt') as f:
        packets = bubble_sort([ast.literal_eval(packet) for packet in f.read().split("\n") if packet != ""] + dividers)

    for packet in packets:
        logging.info(packet)

    # -------------------------------------------------------------------------
    # RESULTS
    # -------------------------------------------------------------------------
    logging.info('-------------------------------------------------------------')
    for index, divider in enumerate(dividers):
        logging.info(f"Divider {index + 1}: {divider}, index: {packets.index(divider)}")

    logging.info(f"Decoder key: {math.prod([(packets.index(divider) + 1) for divider in dividers])}")
