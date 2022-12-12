import json
import logging
import re


# -----------------------------------------------------------------------------
# INIT
# -----------------------------------------------------------------------------
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()
file_handler = logging.FileHandler("day-11-part-1.log", mode="w")
logger.addHandler(file_handler)
# logger.handlers = [handler for handler in logger.handlers if not type(handler) == logging.StreamHandler]

monkeys = []
ROUNDS = 20


# -----------------------------------------------------------------------------
# MONKEYOPERATION
# -----------------------------------------------------------------------------
class MonkeyOperation():

    PATTERNS = {
        'operation': re.compile(r"^(old|[0-9]*) ([*/\-+]) (old|[0-9]*)$")
    }

    def __init__(self, input):
        self.parse(input)

    def parse(self, input):
        self.left, self.operator, self.right = MonkeyOperation.PATTERNS['operation'].match(input).groups()

        try:
            self.left = int(self.left)
        except Exception:
            pass

        try:
            self.right = int(self.right)
        except Exception:
            pass

    def process(self, old):

        #
        # Some assumptions on input here...
        #
        left = self.left if isinstance(self.left, int) else old
        right = self.right if isinstance(self.right, int) else old

        if self.operator == "+":
            return left + right
        elif self.operator == "-":
            return left - right
        elif self.operator == "*":
            return left * right
        elif self.operator == "/":
            return int(left / right)
        else:
            raise Exception(f"Failed to process operation {self.__str__()}")

    def __repr__(self):
        return {
            'left': self.left,
            'operator': self.operator,
            'right': self.right
        }

    def __str__(self):
        return json.dumps(self.__repr__(), indent=2)


# -----------------------------------------------------------------------------
# MONKEYTEST
# -----------------------------------------------------------------------------
class MonkeyTest():

    PATTERNS = {
        'divisor': re.compile(r"^  Test: divisible by ([0-9]*)$"),
        'true': re.compile(r"^    If true: throw to monkey ([0-9]*)$"),
        'false': re.compile(r"^    If false: throw to monkey ([0-9]*)$")
    }

    def __init__(self, input):
        self.parse(input)

    def parse(self, input):
        self.divisor = int(MonkeyTest.PATTERNS['divisor'].match(input[0]).groups()[0])
        self.true = int(MonkeyTest.PATTERNS['true'].match(input[1]).groups()[0])
        self.false = int(MonkeyTest.PATTERNS['false'].match(input[2]).groups()[0])

    def process(self, value):
        if value % self.divisor == 0:
            return self.true
        else:
            return self.false

    def __repr__(self):
        return {
            'divisor': self.divisor,
            'true': self.true,
            'false': self.false
        }

    def __str__(self):
        return json.dumps(self.__repr__(), indent=2)


# -----------------------------------------------------------------------------
# MONKEY
# -----------------------------------------------------------------------------
class Monkey():

    PATTERNS = {
        'id': re.compile(r"^Monkey ([0-9]*):$"),
        'items': re.compile(r"^  Starting items: ([0-9, ]*)$"),
        'operation': re.compile(r"^  Operation: new = (.*)$")
    }

    def __init__(self, input_string):
        self.inspections = 0
        self.parse(input_string.split("\n"))

    def inspect(self):

        while self.items:

            self.inspections += 1
            item = self.items.pop(0)
            item = self.operation.process(item)
            item = int(item / 3)
            target = self.test.process(item)

            yield(item, target)

    def parse(self, input):

        try:

            self.id = int(Monkey.PATTERNS['id'].match(input[0]).groups()[0])
            self.items = [int(item) for item in Monkey.PATTERNS['items'].match(input[1]).groups()[0].split(",")]
            self.operation = MonkeyOperation(Monkey.PATTERNS['operation'].match(input[2]).groups()[0])
            self.test = MonkeyTest(input[3:6])

        except Exception as e:
            logging.error(f"Failed to parse input for Monkey: {input}, {repr(e)}")

    def __repr__(self):
        return {
            'id': self.id,
            'items': self.items,
            'operation': self.operation.__repr__(),
            'test': self.test.__repr__()
        }

    def __str__(self):
        return json.dumps(self.__repr__(), indent=2)


# -----------------------------------------------------------------------------
# MAIN
# -----------------------------------------------------------------------------
if __name__ == '__main__':

    with open('input.txt') as f:
        for monkey in [chunk for chunk in f.read().split("\n\n")]:
            monkeys.append(Monkey(monkey))

    #
    # Loop through rounds
    #
    for round in range(0, ROUNDS):

        #
        # Loop through monkeys
        #
        for monkey in monkeys:

            #
            # Process inspections and throw item to another monkey
            #
            logging.info(monkey)
            for item, target in monkey.inspect():
                monkeys[target].items.append(item)

    # -------------------------------------------------------------------------
    # RESULTS
    # -------------------------------------------------------------------------
    logging.info('-------------------------------------------------------------')
    for monkey in monkeys:
        logging.info(f"Monkey {monkey.id}: [{monkey.inspections}] {monkey.items}")
    logging.info('-------------------------------------------------------------')
    monkeys.sort(key=lambda monkey: monkey.inspections, reverse=True)
    logging.info(f"Monkey business: {monkeys[0].inspections * monkeys[1].inspections}")
    logging.info('-------------------------------------------------------------')
