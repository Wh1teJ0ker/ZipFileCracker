"""Logging components."""

import time
from math import floor
from typing import TextIO

from zipCracker.util.datetime import format_struct_time

initialized: bool = False

LOG_PATH_DEFAULT: str = "logs"
LOGFILE_DEFAULT: str = "cracker"
LOG_HEADER: dict[str, str] = {"error": "Error", "warn": "Warning", "info": "Info", "debug": "Debug"}
"""A dictionary representing all available logging levels (presets)."""

logfile: TextIO
"""The log file IO stream."""


def init() -> None:
    """
    Initialize the logging module and open the file for logging.
    The default log name is `cracker-<Time in seconds>.log`.

    初始化日志模块，并打开日志文件。默认文件名如上。
    """
    global initialized
    global logfile

    full_file_name: str = f"{LOGFILE_DEFAULT}-{floor(time.time())}.log"

    try:
        logfile = open(full_file_name, "w", encoding="utf-8")
        initialized = True
        log("info", __name__, "Logger initialized")

    except IOError as e:
        print(e)
        print("Error creating the log file. The log would not be recorded.")


def cleanup() -> None:
    """
    Close the logging file stream.

    关闭日志文件流。
    """
    global logfile
    global initialized

    try:
        logfile.close()
    except NameError or IOError as e:
        print(e)
        print("Cannot close the log file. Leaving it as-is!")
        pass
    finally:
        initialized = False


def log(level: str, module: str, message: str) -> None:
    """
    A general interface for logging.
    This function is used by other specific log functions.

    日志通用接口，被其他特定日志函数使用。
    """
    global logfile

    if initialized is not True:
        return

    log_level: str

    # Read headers from dictionary first, then fall back to `level` if unavailable
    try:
        log_level = LOG_HEADER[level]
    except KeyError:
        log_level = level

    logfile.write(f"[{log_level}] {module}@{format_struct_time(time.localtime())}: {message}\n")


def info(message: str, module: str) -> None:
    """
    Log an information message.

    记录信息级消息。
    """
    log("info", module, message)


def warn(message: str, module: str) -> None:
    """
    Log a warning message.

    记录警告级消息。
    """
    log("warn", module, message)


def error(message: str, module: str) -> None:
    """
    Log an error message.

    记录错误级消息。
    """
    log("error", module, message)


def debug(message: str, module: str) -> None:
    """
    Log a debug message.
    This should be written into the log file only with the corresponding switch on.

    记录调试级消息，应仅在调试开关打开时写入。
    """
    log("debug", module, message)
