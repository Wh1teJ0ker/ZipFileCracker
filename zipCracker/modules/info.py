"""Get basic information about a specific archive file."""

import zipfile
import zipCracker.util.logger as logger
import zipCracker.util.cli as cli

__description__ = """Get basic information about a specific archive file.
获取指定压缩文件的基本信息。"""

__usage__ = """Usage: info <archive file>
用法：info <压缩文件>"""

__doc__ = f"""info: {__description__}

{__usage__}"""

__commands__ = {
    # TODO
}

zip_info: dict[str, str] = {}


def detect_archive_format(file_path: str):
    """
    Detect the archive format of a file.
    """
    try:
        f = open(file_path, errors="ignore")
        zip_info["Encoding"] = f.encoding

        header: str = f.read(4)

        f.close()

        # Detect file format based on header data
        if header[:2] == "\x50\x4b":
            get_zip_info(file_path)
        elif header == "\x52\x61\x72\x21":
            get_rar_info(file_path)
        elif header[:2] == "\x37\x7a":
            get_7z_info(file_path)
        else:
            cli.print_and_log(f"Cannot detect file format by its structure. Falling back to file extensions...",
                              "warn", __name__)
            # Fallback: Use file extensions to detect
            if file_path.lower().endswith(".zip"):
                get_zip_info(file_path)
            elif file_path.lower().endswith(".rar"):
                get_rar_info(file_path)
            elif file_path.lower().endswith(".7z"):
                get_7z_info(file_path)
            else:
                cli.print_and_log(f"The file {file_path} isn't supported yet.", "error", __name__)
    except NotImplementedError:
        cli.print_and_log(f"The file {file_path} format isn't supported yet.", "error", __name__)
        cli.exit_with_code(1)
    except FileNotFoundError:
        cli.print_and_log(f"The file {file_path} does not exist.", "error", __name__)
        cli.exit_with_code(1)
    except IOError:
        cli.print_and_log(f"The file {file_path} cannot be opened.", "error", __name__)
        cli.exit_with_code(128)
    return 0


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
        detect_archive_format(args[0])
