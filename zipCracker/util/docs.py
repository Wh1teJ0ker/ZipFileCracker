"""Some constant strings and utilities for documents."""

import zipCracker
import zipCracker.core
import zipCracker.util.cli as cli
from zipCracker.core import get_module
from zipCracker.modules import ALL_MODULES
from zipCracker.util import COLORS

DESCRIPTION = "A simple zip file cracker."


def print_version():
    """
    Print project version information.

    输出项目版本信息。
    """
    print(
        f"""ZipFileCracker version {zipCracker.__version__}
By {" & ".join(zipCracker.__authors__)}, licensed under {zipCracker.__license__}
{DESCRIPTION}
"""
    )


def print_help_list():
    """
    Get a list of available commands and their usage if possible.
    """
    cli.print_and_log("Available commands:", module=__name__)
    
    for i in ALL_MODULES:
        info: str = f"  {i}"
        mod = get_module(i)
        if mod is None:
            info += f" ({COLORS['red']}Not Loaded{COLORS['reset']})"
        else:
            if hasattr(mod, "__description__"):
                info += f" - {mod.__description__}"

        cli.print_and_log(info, module=__name__)
        
    cli.print_and_log(f"Use {COLORS['blue']}zipCracker <command> help{COLORS['reset']}"
                      f" to get detailed usage about a specific command.", module=__name__)
    return


def print_help(module: str):
    """
    Print the help text for a specified module.
    """
    if module == "help":
        print_help_list()
        return

    mod = zipCracker.core.get_module(module)
    
    if mod is None:
        cli.print_and_log(f"The module {module} doesn't exist.", "error", __name__)
    else:
        if not hasattr(mod, "__doc__"):
            cli.print_and_log(f"The module {module} doesn't have a valid doc string.", "warn", __name__)
        else:
            cli.print_and_log(getattr(mod, "__doc__"), "info", __name__)
