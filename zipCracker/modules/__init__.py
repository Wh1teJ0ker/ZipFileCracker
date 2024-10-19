"""
All features of the cracker would be separated into several files here.
Import modules you are about to use below.
"""
import zipCracker
import zipCracker.util.logger as logger
import zipCracker.util.cli as cli

PREFIX = "zipCracker.modules."
ALL_MODULES: list[str] = ["info"]
"""Modules to be loaded. Must use full name."""

COMMANDS: dict[str, str]


def load_modules():
    """
    Load all modules in the list ALL_MODULES for later use.
    """
    for module in ALL_MODULES:
        try:
            loaded_module = __import__(PREFIX + module)
            logger.info(f"Loading module: {module}", __name__)

            if not hasattr(loaded_module, "__description__") or not hasattr(loaded_module, "__doc__"):
                logger.info(f"{module} doesn't have an available description or document. "
                            f"It's suggested to add them to clarify the use of this module.",
                            __name__)
        except ImportError as e:
            cli.print_and_log(f"Failed to import module: {module}, because: {e.msg}",
                              "error", __name__)


def load_command():
    # TODO
    return 0


def call(module: str, args: list[str]):
    """
    Call a specific module to handle subsequent processes.
    """
    if module not in ALL_MODULES:
        cli.print_and_log(f"Module not found: {module}", "error", __name__)
        cli.exit_with_code(1)
    else:
        mod = getattr(zipCracker.modules, module)
        try:
            mod.run(args)
        except AttributeError:
            cli.print_and_log(f"The module {module} doesn't have a valid entry.", "error", __name__)
            cli.exit_with_code(1)
