"""Main process unit."""

import sys
from zipCracker import __version__, __authors__, __license__
from zipCracker.util import logger
from zipCracker.util import docs

def main():
    ARGS: list[str] = sys.argv[1:]
    if len(ARGS) == 0:
        docs.printVersion()
    print(ARGS)
