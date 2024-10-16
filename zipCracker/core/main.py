"""Main process unit."""

import sys
from zipCracker import __version__, __authors__, __license__
from zipCracker.util import logger
# from zipCracker.util import cli
from zipCracker.util import docs


def main():
    args: list[str] = sys.argv[1:]
    logger.debug(f"Command line arguments: {args}", "Main")

    if len(args) == 0:
        docs.printVersion()
