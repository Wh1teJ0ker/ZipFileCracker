"""Some constant strings and utilities for documents."""

import zipCracker

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


def print_help():
    # TODO
    return
