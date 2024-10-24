"""The core components of the zipCracker project."""
from zipCracker import modules as modules
from zipCracker.util import logger


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
