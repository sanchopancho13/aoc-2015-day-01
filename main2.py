from __future__ import annotations

import sys
import logging
import time

from solutions.part2 import solution2
from util.utils import entry_point

LOG = logging.getLogger(__name__)

@entry_point
def main():
    # read file
    input: str = ""
    with open(sys.argv[1], "r") as file:
        for line in file:
            stripped = line.strip()
            if stripped:
                input = stripped
                break

    # invoke solution
    result = solution2(input)

    LOG.info("Result: %s", result)

if __name__ == "__main__":
    main()
