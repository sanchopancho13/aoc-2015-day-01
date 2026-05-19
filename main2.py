from __future__ import annotations

import sys
import logging
import time
from turtle import position

from solutions.part2 import get_basement_position
from util.utils import entry_point

LOG = logging.getLogger(__name__)

@entry_point
def main():
    # read file
    instructions: str = ""
    with open(sys.argv[1], "r") as file:
        for line in file:
            stripped = line.strip()
            if stripped:
                instructions = stripped
                break

    # invoke solution
    position = get_basement_position(instructions)

    LOG.info("Position: %s", position)

if __name__ == "__main__":
    main()
