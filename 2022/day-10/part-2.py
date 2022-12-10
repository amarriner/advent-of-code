import logging


#
# INIT
#
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()
file_handler = logging.FileHandler("day-10-part-1.log", mode="w")
logger.addHandler(file_handler)
# logger.handlers = [handler for handler in logger.handlers if not type(handler) == logging.StreamHandler]

CRT_HEIGHT = 6
CRT_WIDTH = 40
clock = 1
register = 1
display = [["." for i in range(0, CRT_WIDTH)] for j in range(0, CRT_HEIGHT)]


#
# HELPERS
#
def tick(clock, register, display):

    pixel = "."
    col = clock % CRT_WIDTH
    row = int(clock / CRT_WIDTH)
    if register in range(col - 1, col + 2):
        pixel = "#"

    if clock < 240:
        logging.debug(f"Clock: {clock}, {int(clock / CRT_WIDTH)}, {clock % CRT_WIDTH}")
        display[row][col] = pixel

    return clock + 1


#
# MAIN
#
if __name__ == '__main__':

    with open('input.txt') as f:
        lines = [line for line in f.read().split("\n") if line != ""]

    for line in lines:

        clock = tick(clock, register, display)

        if line.startswith('addx'):

            x = int(line.split(" ")[1])
            register += x

            clock = tick(clock, register, display)

    logging.info('-------------------------------------------------------------')
    logging.info(f'Clock   : {clock}')
    logging.info(f'Register: {register}')
    logging.info('-------------------------------------------------------------')
    logging.info("\n" + "\n".join(["".join(line) for line in display]))
    logging.info('-------------------------------------------------------------')
