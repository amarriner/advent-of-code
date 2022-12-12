import json
import logging
import string


# -----------------------------------------------------------------------------
# INIT
# -----------------------------------------------------------------------------
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()
file_handler = logging.FileHandler("day-12-part-2.log", mode="w")
logger.addHandler(file_handler)
# logger.handlers = [handler for handler in logger.handlers if not type(handler) == logging.StreamHandler]

INFINITY = 1000000


# -----------------------------------------------------------------------------
# CLASSES
# -----------------------------------------------------------------------------
class Point():
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def __repr__(self):
        return self.__dict__

    def __str__(self):
        return json.dumps(self.__repr__())

    def __eq__(self, other):
        return self.row == other.row and self.col == other.col


class Node():
    def __init__(self, point, weight, distance):
        self.point = point
        self.weight = weight
        self.visited = False
        self.distance = distance

    def __repr__(self):
        return self.__dict__

    def __str__(self):
        return json.dumps(self.__repr__())


class Grid():
    def __init__(self):
        self.nodes = []
        self.end = None
        self.current = None

    def __repr__(self):
        return self.__dict__

    def __str__(self):
        return json.dumps(self.__repr__())


# -----------------------------------------------------------------------------
# HELPERS
# -----------------------------------------------------------------------------
def shortest_path(grid, queue):

    while queue:

        queue.sort(key=lambda item: grid.nodes[item.row][item.col].distance)
        grid.current = queue.pop(0)
        if grid.nodes[grid.current.row][grid.current.col].distance == INFINITY:
            break

        right = Point(grid.current.row, grid.current.col + 1)
        if right in queue:
            logging.debug(f"Updating right {right} [{grid.nodes[right.row][right.col].weight}] from {grid.current} [{grid.nodes[grid.current.row][grid.current.col].weight}] to {grid.nodes[grid.current.row][grid.current.col].distance + 1}")
            if grid.nodes[right.row][right.col].weight <= grid.nodes[grid.current.row][grid.current.col].weight + 1:
                if grid.nodes[right.row][right.col].distance > grid.nodes[grid.current.row][grid.current.col].distance + 1:
                    grid.nodes[right.row][right.col].distance = grid.nodes[grid.current.row][grid.current.col].distance + 1

        left = Point(grid.current.row, grid.current.col - 1)
        if left in queue:
            logging.debug(f"Updating left {left} [{grid.nodes[left.row][left.col].weight}] from {grid.current} [{grid.nodes[grid.current.row][grid.current.col].weight}] to {grid.nodes[grid.current.row][grid.current.col].distance + 1}")
            if grid.nodes[left.row][left.col].weight <= grid.nodes[grid.current.row][grid.current.col].weight + 1:
                if grid.nodes[left.row][left.col].distance > grid.nodes[grid.current.row][grid.current.col].distance + 1:
                    grid.nodes[left.row][left.col].distance = grid.nodes[grid.current.row][grid.current.col].distance + 1

        up = Point(grid.current.row - 1, grid.current.col)
        if up in queue:
            logging.debug(f"Updating up {up} [{grid.nodes[up.row][up.col].weight}] from {grid.current} [{grid.nodes[grid.current.row][grid.current.col].weight}] to {grid.nodes[grid.current.row][grid.current.col].distance + 1}")
            if grid.nodes[up.row][up.col].weight <= grid.nodes[grid.current.row][grid.current.col].weight + 1:
                if grid.nodes[up.row][up.col].distance > grid.nodes[grid.current.row][grid.current.col].distance + 1:
                    grid.nodes[up.row][up.col].distance = grid.nodes[grid.current.row][grid.current.col].distance + 1

        down = Point(grid.current.row + 1, grid.current.col)
        if down in queue:
            logging.debug(f"Updating down {down} [{grid.nodes[down.row][down.col].weight}] from {grid.current} [{grid.nodes[grid.current.row][grid.current.col].weight}] to {grid.nodes[grid.current.row][grid.current.col].distance + 1}")
            if grid.nodes[down.row][down.col].weight <= grid.nodes[grid.current.row][grid.current.col].weight + 1:
                if grid.nodes[down.row][down.col].distance > grid.nodes[grid.current.row][grid.current.col].distance + 1:
                    grid.nodes[down.row][down.col].distance = grid.nodes[grid.current.row][grid.current.col].distance + 1

    return grid


# -----------------------------------------------------------------------------
# MAIN
# -----------------------------------------------------------------------------
if __name__ == '__main__':

    starts = []
    queue = []
    grid = Grid()
    with open('input.txt') as f:

        for row, line in enumerate(f.read().split("\n")):

            grid.nodes.append([])

            for col, char in enumerate(line):

                start = False
                distance = INFINITY
                if char in ['a', 'S']:
                    starts.append(Point(row, col))
                    distance = 0
                    char = 'a'
                    start = True
                elif char == 'E':
                    grid.end = Point(row, col)
                    char = 'z'

                if not start:
                    queue.append(Point(row, col))

                grid.nodes[row].append(Node(Point(row, col), string.ascii_lowercase.index(char), distance))

    shortest = []
    for start in starts:
        logging.info(start)
        grid = shortest_path(grid, queue + [start])

        distance = grid.nodes[grid.end.row][grid.end.col].distance
        if distance not in shortest:
            shortest.append(distance)

    shortest.sort()
    logging.info(shortest)

    # -------------------------------------------------------------------------
    # RESULTS
    # -------------------------------------------------------------------------
    logging.info('-------------------------------------------------------------')
    logging.info(f'End                 : {grid.end}')
    logging.info(f'Current             : {grid.current}')
    logging.info(f'Grid                : {len(grid.nodes)} rows, {len(grid.nodes[0])} cols')
    logging.info(f'Shortests           : {shortest[-1]}')
    logging.debug(grid)
