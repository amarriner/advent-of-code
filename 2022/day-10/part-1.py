import logging


#
# INIT
#
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()
file_handler = logging.FileHandler("day-10-part-1.log", mode="w")
logger.addHandler(file_handler)
# logger.handlers = [handler for handler in logger.handlers if not type(handler) == logging.StreamHandler]

clock = 1
register = 1
strengths = []


#
# HELPERS
#
def tick(clock, register, strengths):
    clock += 1

    if (clock + 20) % 40 == 0 and clock <= 220:
        strengths.append(clock * register)

    return clock


#
# MAIN
#
if __name__ == '__main__':

    with open('input.txt') as f:
        lines = [line for line in f.read().split("\n") if line != ""]

    for line in lines:

        logging.debug(f"--> Clock: {clock}; register {register}; strengths {strengths}")
        logging.debug(f"[ ] Clock: {clock}; register {register}; strengths {strengths}")
        clock = tick(clock, register, strengths)

        if line.startswith('addx'):

            x = int(line.split(" ")[1])
            register += x

            logging.debug(f"[A] Clock: {clock}; register {register}; strengths {strengths}")
            clock = tick(clock, register, strengths)

    logging.info('-------------------------------------------------------------')
    logging.info(f'Register: {register}')
    logging.info(f'Strengths: {strengths}, sum: {sum(strengths)}')
