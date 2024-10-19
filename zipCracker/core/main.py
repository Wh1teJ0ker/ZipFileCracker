"""Main process unit."""

import sys
from zipCracker.util import logger
# from zipCracker.util import cli
from zipCracker.util import docs
from zipCracker.util import cli

# A module must be imported to be found by getattr.
import zipCracker.modules as modules


def main():
    args: list[str] = sys.argv[1:]
    logger.debug(f"Command line arguments: {args}", "Main")
    modules.load_modules()

    if len(args) == 0:
        cli.print_and_log(msg="Specify a command first. Execute with -h to get a list of commands.",
                          level="warn", module=__name__)
    else:
        if args.__contains__("--version"):
            if len(args) > 1:
                cli.print_and_log(msg="Too many arguments for --version", level="error", module=__name__)
            else:
                docs.print_version()
        elif args.__contains__("--help"):
            # TODO: Get help content for individual modules
            docs.print_help()
        else:
            modules.call(args[0], args[1:])


def get_module(name: str):
    """
    Returns a module with the given name.
    If the module is not found, None is returned.
    """
    try:
        return getattr(modules, name)
    except AttributeError:
        logger.error(f"Module not found: {name}", __name__)
        return None
