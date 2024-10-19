"""The base of the cracker."""

# Simple information about the project
__license__ = "MIT"
__version__ = "0.0.1 alpha"
__authors__ = ["CloneWith", "Wh1teJ0ker"]
__website__ = "https://github.com/Wh1teJ0ker/ZipFileCracker"

from zipCracker import core
from zipCracker.util import logger
import zipCracker.core.main


def launch() -> None:
    """
    Prepare the basic framework, then call the main module.
    """
    # Prepare for loggers and command line interface here
    logger.init()
    # Get the main function up and running!
    zipCracker.core.main.main()

    # After the main function close the log file.
    logger.cleanup()
