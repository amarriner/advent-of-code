import json
import logging


# -----------------------------------------------------------------------------
# INIT
# -----------------------------------------------------------------------------
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()
file_handler = logging.FileHandler("day-14-part-2.log", mode="w")
logger.addHandler(file_handler)
# logger.handlers = [handler for handler in logger.handlers if not type(handler) == logging.StreamHandler]

GRID_SIZE = 10000


# -----------------------------------------------------------------------------
# CLASSES
# -----------------------------------------------------------------------------
class Point():
    def __init__(self, input=None, x=None, y=None):

        if input is not None:
            self.x = int(input.split(",")[0])
            self.y = int(input.split(",")[1])

        if x is not None:
            self.x = x

        if y is not None:
            self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __str__(self):
        return json.dumps({
            'x': self.x,
            'y': self.y
        }, indent=2)


class Cave():

    def __init__(self, paths):

        self.grid = [['.' for i in range(0, GRID_SIZE)] for j in range(0, GRID_SIZE)]
        self.paths = paths
        self.sand_start = Point(x=500, y=0)
        self.build()
        self.flow()

    def build(self):

        self.highest_x = 0
        self.highest_y = 0
        self.lowest_x = 1000000000
        self.lowest_y = 1000000000
        for line_index, line in enumerate(self.paths):

            last_point = None
            logging.info(line)
            for point_index, point in enumerate(line):

                if last_point is None:
                    self.grid[point.y][point.x] = "#"

                else:

                    j_increment = -1 if last_point.y > point.y else 1
                    for j in range(last_point.y, point.y + j_increment, j_increment):
                        logging.debug(f"(j: {j}) [{line_index} - {point_index}] {repr(last_point)} -> {repr(point)} setting {j},{last_point.x} = '#'")
                        self.grid[j][last_point.x] = "#"

                    i_increment = -1 if last_point.x > point.x else 1
                    for i in range(last_point.x, point.x + i_increment, i_increment):
                        logging.debug(f"(i: {i}) [{line_index} - {point_index}] {repr(last_point)} -> {repr(point)} setting {last_point.y},{i} = '#'")
                        self.grid[last_point.y][i] = "#"

                last_point = point

                if last_point.x > self.highest_x:
                    self.highest_x = last_point.x
                if last_point.y > self.highest_y:
                    self.highest_y = last_point.y
                if last_point.x < self.lowest_x and last_point.x >= 0:
                    self.lowest_x = last_point.x
                if last_point.y < self.lowest_y and last_point.y >= 0:
                    self.lowest_y = last_point.y

        logging.info(f"Highest: {self.highest_x}, {self.highest_y}")
        logging.info(f"Lowest : {self.lowest_x}, {self.lowest_y}")
        self.lowest_x = self.lowest_x - 5 if self.lowest_x - 5 > 0 else 0
        self.lowest_y = self.lowest_y - 5 if self.lowest_y - 5 > 0 else 0

        self.floor = self.highest_y + 2
        logging.info(f"Floor   : {self.floor}")
        for i in range(0, len(self.grid[self.floor])):
            self.grid[self.floor][i] = '#'
        self.highest_y += 2

        self.grid[self.sand_start.y][self.sand_start.x] = "+"

    def flow(self):

        self.grains = 0
        full = False
        while not full:

            grain = Point(x=self.sand_start.x, y=self.sand_start.y)

            while True:

                if self.grid[self.sand_start.y][self.sand_start.x] == 'o':
                    logging.info(f"Found the end after {self.grains} grains of sand")
                    full = True
                    break

                next = self.grid[grain.y + 1][grain.x]

                # Empty space, continue to fall
                if next == '.':
                    grain.y += 1
                    continue

                # Check diagonals
                elif next != '.':

                    if self.grid[grain.y + 1][grain.x - 1] == '.':
                        grain.y += 1
                        grain.x -= 1
                        continue

                    if self.grid[grain.y + 1][grain.x + 1] == '.':
                        grain.y += 1
                        grain.x += 1
                        continue

                    self.grid[grain.y][grain.x] = 'o'
                    self.grains += 1
                    break

    def __str__(self):
        return "\n" + "\n".join(["".join(line[self.lowest_x:self.highest_x + 5]) for line in self.grid[self.lowest_y:self.highest_y + 5]])

# -----------------------------------------------------------------------------
# HELPERS
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# MAIN
# -----------------------------------------------------------------------------
if __name__ == '__main__':

    with open('input.txt') as f:
        cave = Cave([[Point(input=point) for point in line.split(" -> ")] for line in f.read().split("\n") if line != ""])

    # -------------------------------------------------------------------------
    # RESULTS
    # -------------------------------------------------------------------------
    logging.info('-------------------------------------------------------------')
    logging.info(cave.paths)
    logging.info(cave)
