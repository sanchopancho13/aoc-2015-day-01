import logging

LOG = logging.getLogger(__name__)

def get_floor(instructions: str) -> int:
    floor = 0
    for c in instructions:
        if c == "(":
            floor += 1
        elif c == ")":
            floor -= 1
    return floor
