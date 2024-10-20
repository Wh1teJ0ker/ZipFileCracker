"""Check for fake encryption by reading archive file headers."""

import zipfile
import zipCracker.util.cli as cli

__description__ = """Check for encryption by reading archive file headers.
读取压缩文件头，检测加密情况。"""

__usage__ = """Usage: headcrack <archive file>
用法：headcrack <压缩文件>"""

__doc__ = f"""headcrack: {__description__}

{__usage__}"""


def judge_zip(file_path: str):
    """
    Check if the ZIP archive has fake encryption.
    检查zip文件是否存在伪加密
    """
    try:
        zf = zipfile.ZipFile(file_path)
        for info in zf.infolist():
            if info.flag_bits & 0x1:
                cli.print_and_log(f"Got the flag bit: {info.flag_bits}", module=__name__)
                zf.close()
                return True
        zf.close()
        return False
    except zipfile.BadZipFile:
        cli.print_and_log(f"The file {file_path} is not a valid ZIP file.", "error", __name__)
        cli.exit_with_code(1)
    except zipfile.error as e:
        cli.print_and_log(f"An error occurred while trying to read the file {file_path}: {e}",
                          "error", __name__)
        cli.exit_with_code(127)
    except FileNotFoundError:
        cli.print_and_log(f"File not found: {file_path}", "error", __name__)
        cli.exit_with_code(1)


def judge_rar(file_path: str):
    """
    Check if the RAR archive has fake encryption.
    检查rar文件是否存在伪加密
    """
    raise NotImplementedError


def run(args: list[str]):
    if len(args) == 0 or "-h" in args or "--help" in args:
        cli.print_and_log(__doc__, "warn", __name__)
    elif len(args) >= 2:
        cli.print_and_log(f"Too many arguments, expecting 1, got {len(args)}", "error", __name__)
    else:
        zip_path: str = args[0]
        if judge_zip(zip_path):
            cli.print_and_log(f"Possible encryption detected in {zip_path}", module=__name__)
        else:
            cli.print_and_log(f"No encryption found in {zip_path}", module=__name__)
