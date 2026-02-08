"""Docstring for utils."""

from dataclasses import dataclass

# import os, sys  # noqa: ERA001


@dataclass
class Listing:
    """Data class for Listing."""

    def __init__(self, d: int) -> None:
        """Docstring for __init__.

        :param self: Description
        :param d: Description
        :type d: int
        """

    def do_this(self) -> int:
        """Docstring for do_this.

        :return: param containing xyz
        """
        return 1
