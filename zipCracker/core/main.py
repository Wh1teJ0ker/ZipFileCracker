"""Main process unit."""

import sys
from zipCracker.util import logger
# from zipCracker.util import cli
from zipCracker.util import docs
from zipCracker.util import cli

# A module must be imported to be found by getattr.
import zipCracker.modules as modules


def get_nonswitch_arg(args: list[str]):
    """
    Extract commands and their arguments for later use.

    提取命令及其参数，以供后续使用。
    """
    flag: bool = False
    pure_args: list[str] = []

    for arg in args:
        if not arg.startswith('-') or flag:
            flag = True
            pure_args.append(arg)
    return pure_args


def main():
    args: list[str] = sys.argv[1:]
    logger.debug(f"Command line arguments: {args}", "Main")
    modules.load_modules()

    if len(args) == 0:
        cli.print_and_log(msg="Specify a command first. Execute with -h to get a list of commands.",
                          level="warn", module=__name__)
    else:
        if "-v" or "--verbose" in args:
            # Enable debug logging and output.
            # Verbose switch applys to the main module itself.
            # 启用调试信息的记录与输出，应用到全局。
            logger.log_debug = True
            cli.ARG_VERBOSE = True
        if "--version" in args:
            if len(args) > 1:
                cli.print_and_log(msg="Too many arguments for --version", level="error", module=__name__)
            else:
                docs.print_version()
        elif len(args) == 1 and ("--help" or "-h" in args):
            # TODO: Get help content for individual modules
            # TODO: 获取各个模块的帮助内容
            docs.print_help()
        else:
            pure_args = get_nonswitch_arg(args)
            logger.debug(f"Calling module {pure_args[0]} with argument {pure_args[1:]}", __name__)
            modules.call(pure_args[0], pure_args[1:])


def get_module(name: str):
    """
    Returns a module with the given name.
    If the module is not found, None is returned.

    返回给定名称的模块，若找不到则返回 None。
    """
    try:
        return getattr(modules, name)
    except AttributeError:
        logger.error(f"Module not found: {name}", __name__)
        return None
