"""Handles date and time formatting and manipulation."""

import time


def format_struct_time(struct: time.struct_time) -> str:
    """
    Transform a `time.struct_time` into a string designed for logging and general displaying.
    The format is like `11450919-19:19:08`.
    """
    return (f"{struct.tm_year:04d}{struct.tm_mon:02d}{struct.tm_mday:02d}-"
            f"{struct.tm_hour:02d}:{struct.tm_min:02d}:{struct.tm_sec:02d}")
