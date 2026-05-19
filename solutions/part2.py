import logging

LOG = logging.getLogger(__name__)

def get_basement_position(instructions: str) -> int:
    floor = 0
    for i, c in enumerate(instructions):
        if c == "(":
            floor += 1
        elif c == ")":
            floor -= 1
        if floor == -1:
            return i + 1
    return -1
