import logging
import re
import sys


logging.basicConfig(stream=sys.stdout, level=logging.INFO)

CD_PATTERN = re.compile(r'^\$ cd (.*)$')
LS_PATTERN = re.compile(r'^\$ ls.*$')
THRESHOLD = 30000000
CAPACITY = 70000000


def cd(structure, cwd, directory):

    logging.debug(f'Changing dir from {cwd} to {directory}')

    if directory == "..":
        return "/".join(cwd.split("/")[:-1])

    elif directory == "/":
        return directory

    else:
        if cwd == '/':
            newdir = f'/{directory}'
        else:
            newdir = f'{cwd}/{directory}'

        if newdir not in structure:
            structure[newdir] = {}

        return newdir


def get_size(structure, directory):

    size = 0
    for dir in [dir for dir in structure if dir.startswith(directory)]:
        size += sum([structure[dir][file] for file in structure[dir]])

    return size


def ls(structure, cwd, contents):

    size, name = contents.split(" ")
    if size != "dir":
        structure[cwd][name] = int(size)


if __name__ == '__main__':

    with open('input.txt') as f:
        lines = [line for line in f.read().split("\n") if line != ""]

    structure = {'/': {}}
    cwd = "/"
    for line in lines:

        logging.debug(line)

        if CD_PATTERN.match(line):
            cwd = cd(structure, cwd, CD_PATTERN.match(line).groups()[0])

        elif not LS_PATTERN.match(line):
            ls(structure, cwd, line)

    root = get_size(structure, "/")
    unused = CAPACITY - root
    needed = THRESHOLD - unused
    logging.info(f'Root dir size: {root}, unused space {unused}, needed {needed}')
    large_dirs = [get_size(structure, dir) for dir in structure if get_size(structure, dir) >= needed]
    large_dirs.sort()
    logging.info(f"Size of directory to remove >= {needed}: {large_dirs[0]}")
