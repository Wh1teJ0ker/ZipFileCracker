"""Simple command line handling."""
import sys

from zipCracker.util import *
from zipCracker.util import logger

ARG_VERBOSE = False
"""
If we should print verbose output.
This is subject to change with command line arguments.
"""

SYM: dict[str, str] = {
    "error": bold(COLORS["red"] + "Error"),
    "warn": bold(COLORS["yellow"] + "Warning"),
    "info": bold(COLORS["blue"] + "Info"),
    "debug": bold("Verbose")
}


def print_and_log(msg: str, level: str = "info", module: str = "Generic", nolog: bool = False):
    """
    Print prettified message and log it when necessary.

    输出格式化消息，必要时记录到日志。
    """

    if level != "debug" or (level == "debug" and ARG_VERBOSE):
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

    使程序做好清理工作后带退出码退出。
    """
    if code is not 0:
        logger.error(f"An error occurred, exiting with code {code}.", __name__)
    else:
        logger.info(f"Program exiting with code {code}.", __name__)

    logger.cleanup()
    sys.exit(code)
