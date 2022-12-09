import logging

from collections import namedtuple


#
# INIT
#
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()
file_handler = logging.FileHandler("day-9-part-1.log", mode="w")
logger.addHandler(file_handler)
logger.handlers = [handler for handler in logger.handlers if not type(handler) == logging.StreamHandler]
Point = namedtuple('Point', 'x y')
head = Point(0, 0)
tail = head
visited = [head]


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
    else:
        return tail


#
# MAIN
#
if __name__ == '__main__':

    with open('input.txt') as f:
        lines = [line for line in f.read().split("\n") if line != ""]

    for direction, iterations in [line.split(" ") for line in lines]:

        logging.info(f"Moving {direction} {iterations} times")

        for i in range(0, int(iterations)):
            head = move_head(head, direction)
            logging.debug(f"Head: {head}")
            tail = move_tail(head, tail)
            logging.debug(f"Tail: {tail}")

            if tail not in visited:
                visited.append(tail)

    logging.info('-------------------------------------------------------------')
    logging.info(f"Head: {head}")
    logging.info(f"Tail: {tail}")
    logging.info(f"Tail visted {len(visited)} points")
