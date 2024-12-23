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
    help_flag = False
    
    args: list[str] = sys.argv[1:]
    logger.debug(f"Command line arguments: {args}", "Main")
    modules.load_modules()

    if len(args) == 0:
        cli.print_and_log(msg="Specify a command first. Execute with -h to get a list of commands.",
                          level="warn", module=__name__)
    else:
        if "--verbose" in args:
            # Enable debug logging and output.
            # Verbose switch applies to the main module itself.
            # 启用调试信息的记录与输出，应用到全局。
            del args[args.index("--verbose")]
            logger.log_debug = True
            cli.ARG_VERBOSE = True
        
        # Replace all help variants into one
        for arg in args:
            arg.replace("--help", "help")
            arg.replace("-h", "help")
            if arg == "help":
                help_flag = True
        
        if "--version" in args:
            docs.print_version()
        elif help_flag:
            docs.print_help(args[args.index("help") - 1])
        else:
            pure_args = get_nonswitch_arg(args)
            logger.debug(f"Calling module {pure_args[0]} with argument {pure_args[1:]}", __name__)
            modules.call(pure_args[0], pure_args[1:])
