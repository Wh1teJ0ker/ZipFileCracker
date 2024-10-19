"""Get basic information about a specific archive file."""

import zipfile
import zipCracker.util.logger as logger
import zipCracker.util.cli as cli

__doc__ = """
Get basic information about a specific archive file.

Usage: info <archive file>
"""

__commands__ = {
    # TODO
}

zip_info: dict[str, str] = {}


def get_zip_info(file_path: str):
    """
    Get basic information of a ZIP file.
    Uses the zipFile module.
    """
    global zip_info

    try:
        with zipfile.ZipFile(file_path) as zf:
            logger.log("info", f"ZIP file opened: {file_path}", __name__)

            zip_info["Name"] = zf.filename
            zip_info["Comment"] = zf.comment.decode()
            zip_info["Compression"] = str(zf.compression)
            zip_info["Compression level"] = str(zf.compresslevel)

        for i in zip_info:
            cli.print_and_log(msg=f"{i}: {zip_info[i]}")

    except zipfile.BadZipFile:
        cli.print_and_log(f"The file {file_path} is not a valid ZIP file.", "error", __name__)
    except zipfile.error as e:
        cli.print_and_log(f"An error occurred while trying to read the file {file_path}: {e}",
                          "error", __name__)


def get_rar_info(file_path: str):
    raise NotImplementedError


def get_7z_info(file_path: str):
    raise NotImplementedError


def run(args: list[str]):
    if len(args) == 0:
        cli.print_and_log(__doc__, "warn", __name__)
    elif len(args) >= 2:
        cli.print_and_log(f"Too many arguments, expecting 1, got {len(args)}", "error", __name__)
    else:
        name = args[0]
        try:
            f = open(name)
            f.close()

            # It feels not precise here. Should judge file formats based on their file structure.
            if name.lower().endswith(".zip"):
                get_zip_info(name)
            elif name.lower().endswith(".rar"):
                get_rar_info(name)
            elif name.lower().endswith(".7z"):
                get_7z_info(name)
            else:
                cli.print_and_log(f"The file {name} isn't supported yet.", "error", __name__)
        except NotImplementedError:
            cli.print_and_log(f"The file {name} format isn't supported yet.", "error", __name__)
            cli.exit_with_code(1)
        except FileNotFoundError:
            cli.print_and_log(f"The file {name} does not exist.", "error", __name__)
            cli.exit_with_code(1)
        except IOError:
            cli.print_and_log(f"The file {name} cannot be opened.", "error", __name__)
            cli.exit_with_code(128)
