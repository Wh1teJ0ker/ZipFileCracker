"""Some constant strings."""

import zipCracker

DESCRIPTION = "A simple zip file cracker."

def printVersion():
    print(
        """ZipFileCracker version {0}
By {1}, licensed under {2}
{3}"""
        .format(
            zipCracker.__version__,
            ", ".join(zipCracker.__authors__),
            zipCracker.__license__,
            DESCRIPTION
        )
    )

def printHelp():
    return
