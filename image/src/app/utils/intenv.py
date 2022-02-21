"""Utility functions for getting the int env variable"""
import os


def intenv(name: str, default=0.0) -> int:
    """ return value from int environment variable otherwise False

    Args:
        name (str): [ENVIRONMENT_VARIABLE]
        default (int, optional): [Fallback value]. Defaults to 0.

    Returns:
        int: [value of the ENVIRONMENT_VARIABLE]
    """
    return int(os.getenv(name)) if os.getenv(name) else default
