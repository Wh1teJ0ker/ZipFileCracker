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


def get_len(s: str) -> int:
    """
    Get the real length of a formatted string.
    """
    real_length: int = len(s)
    mark_regex = re.compile(r"(\033\[(?:[0-9];)?[0-9]+m)+")
    
    match_list = re.findall(mark_regex, s)
    
    for match in match_list:
        real_length -= len(match)
        
    return real_length

def print_and_log(msg: str, level: str = "info", module: str = "Generic", nolog: bool = False, continuous: bool = False):
    """
    Print prettified message and log it when necessary.

    输出格式化消息，必要时记录到日志。
    """

    if level != "debug" or (level == "debug" and ARG_VERBOSE):
        if continuous:
            print(f"{'.' * get_len(SYM[level])}: {msg}")
        else:
            print(f"{SYM[level]}: {msg}")

    if nolog is False:
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
