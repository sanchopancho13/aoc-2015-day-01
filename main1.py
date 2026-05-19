from __future__ import annotations

import sys
import logging
import time

from solutions.part1 import get_floor
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
    floor = get_floor(instructions)

    LOG.info("Floor: %s", floor)

if __name__ == "__main__":
    main()
