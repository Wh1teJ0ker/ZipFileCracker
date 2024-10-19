"""Simple command line handling."""
import sys

from zipCracker.util import COLORS
from zipCracker.util import logger

ARG_VERBOSE = True
"""
If we should print verbose output.
This is subject to change with command line arguments.
"""

COLOR_POST = "\033[0m"
"""A special character sequence to stop coloring and styling."""

SYM: dict[str, str] = {
    "error": COLORS["bold"] + COLORS["red"] + "Error" + COLOR_POST,
    "warn": COLORS["bold"] + COLORS["yellow"] + "Warning" + COLOR_POST,
    "info": COLORS["bold"] + COLORS["blue"] + "Info" + COLOR_POST,
    "debug": "Verbose" + COLOR_POST
}


def print_and_log(msg: str, level: str = "info", module: str = "Generic", nolog: bool = False):
    """
    Print prettified message and log it when necessary.
    """

    print("{0}: {1}".format(SYM[level], msg))

    if nolog is not True:
        try:
            logger_fun = getattr(logger, level)
            logger_fun(msg, module)
        except AttributeError:
            logger.warn(f"The log level {level} is invalid. Falling back to information level.", __name__)
            logger.info(msg, module)


def exit_with_code(code: int):
    """
    Make the program exit gently with an exit code.

    This function would 
    """
    if code is not 0:
        logger.error(f"An error occurred, exiting with code {code}.", __name__)
    else:
        logger.info(f"Program exiting with code {code}.", __name__)

    logger.cleanup()
    sys.exit(code)
