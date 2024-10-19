"""Some constant strings."""

import zipCracker

DESCRIPTION = "A simple zip file cracker."


def print_version():
    print(
        f"""ZipFileCracker version {zipCracker.__version__}
By {" & ".join(zipCracker.__authors__)}, licensed under {zipCracker.__license__}
{DESCRIPTION}
"""
    )


def print_help():
    # TODO
    return
