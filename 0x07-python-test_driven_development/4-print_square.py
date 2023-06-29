#!/usr/bin/python3
"""Defines a square-printing function."""


def print_square(size):
    """Print a square with the # character.

    Args:
        size (int): The square's height and width.
    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for m in range(size):
        [print("#", end="") for o in range(size)]
        print("")
