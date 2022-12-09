import logging

from collections import namedtuple


#
# INIT
#
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()
file_handler = logging.FileHandler("day-9-part-2.log", mode="w")
logger.addHandler(file_handler)
logger.handlers = [handler for handler in logger.handlers if not type(handler) == logging.StreamHandler]
ROPE_LENGTH = 10
Point = namedtuple('Point', 'x y')
rope = [Point(0, 0) for point in range(0, ROPE_LENGTH)]
visited = [rope[0]]


#
# HELPERS
#
def move_head(point, direction):
    if direction == 'U':
        return Point(point.x, point.y - 1)
    elif direction == 'D':
        return Point(point.x, point.y + 1)
    elif direction == 'L':
        return Point(point.x - 1, point.y)
    elif direction == 'R':
        return Point(point.x + 1, point.y)


def move_tail(head, tail):

    # -------------------------------------------------------
    # TODO: There's a MUCH better way to do this, I'm sure by
    #       checking for < or > and not specific numbers
    #       but ... ¯\_(ツ)_/¯
    # -------------------------------------------------------

    #
    # 2 away, cardinal directions
    #
    if head.x == tail.x and head.y - 2 == tail.y:
        return Point(tail.x, tail.y + 1)
    elif head.x == tail.x and head.y + 2 == tail.y:
        return Point(tail.x, tail.y - 1)
    elif head.x - 2 == tail.x and head.y == tail.y:
        return Point(tail.x + 1, tail.y)
    elif head.x + 2 == tail.x and head.y == tail.y:
        return Point(tail.x - 1, tail.y)
    #
    # 2 away in one direction, 1 away in the other
    #
    elif head.x + 2 == tail.x and head.y + 1 == tail.y:
        return Point(tail.x - 1, tail.y - 1)
    elif head.x - 2 == tail.x and head.y + 1 == tail.y:
        return Point(tail.x + 1, tail.y - 1)
    elif head.x + 2 == tail.x and head.y - 1 == tail.y:
        return Point(tail.x - 1, tail.y + 1)
    elif head.x - 2 == tail.x and head.y - 1 == tail.y:
        return Point(tail.x + 1, tail.y + 1)
    elif head.x + 1 == tail.x and head.y + 2 == tail.y:
        return Point(tail.x - 1, tail.y - 1)
    elif head.x - 1 == tail.x and head.y + 2 == tail.y:
        return Point(tail.x + 1, tail.y - 1)
    elif head.x + 1 == tail.x and head.y - 2 == tail.y:
        return Point(tail.x - 1, tail.y + 1)
    elif head.x - 1 == tail.x and head.y - 2 == tail.y:
        return Point(tail.x + 1, tail.y + 1)
    #
    # 2 away in one direction, 2 away in the other
    #
    elif head.x + 2 == tail.x and head.y + 2 == tail.y:
        return Point(tail.x - 1, tail.y - 1)
    elif head.x - 2 == tail.x and head.y + 2 == tail.y:
        return Point(tail.x + 1, tail.y - 1)
    elif head.x + 2 == tail.x and head.y - 2 == tail.y:
        return Point(tail.x - 1, tail.y + 1)
    elif head.x - 2 == tail.x and head.y - 2 == tail.y:
        return Point(tail.x + 1, tail.y + 1)
    elif head.x + 2 == tail.x and head.y + 2 == tail.y:
        return Point(tail.x - 1, tail.y - 1)
    elif head.x - 2 == tail.x and head.y + 2 == tail.y:
        return Point(tail.x + 1, tail.y - 1)
    elif head.x + 2 == tail.x and head.y - 2 == tail.y:
        return Point(tail.x - 1, tail.y + 1)
    elif head.x - 2 == tail.x and head.y - 2 == tail.y:
        return Point(tail.x + 1, tail.y + 1)
    #
    # Otherwise stand still
    #
    else:
        return tail


def print_board(rope):
    for j in range(0, (rope[-1].y + 100)):
        line = ["." for i in range(0, 100)]
        for i in range(0, (rope[-1].x + 100)):
            for index, point in enumerate(rope):
                if point.x + 50 == i and point.y + 50 == j:
                    line[i] = str(index)
        logging.debug("".join(line))
    logging.debug("----------")


#
# MAIN
#
if __name__ == '__main__':

    with open('input.txt') as f:
        lines = [line for line in f.read().split("\n") if line != ""]

    for direction, iterations in [line.split(" ") for line in lines]:

        logging.debug(f"Moving {direction} {iterations} times")

        for i in range(0, int(iterations)):

            rope[0] = move_head(rope[0], direction)
            for j in range(1, ROPE_LENGTH):
                logging.debug(f'{j} Tail start {rope[j]}, head {rope[j - 1]}')
                rope[j] = move_tail(rope[j - 1], rope[j])
                logging.debug(f'{j} Tail end {rope[j]}, head {rope[j - 1]}')

            if rope[-1] not in visited:
                visited.append(rope[-1])

            # print_board(rope)

    logging.info('-------------------------------------------------------------')
    logging.info(f"Tail visted {len(visited)} points")
