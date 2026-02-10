"""Helper modules for backend"""

from dataclasses import dataclass

DEFAULT_REQUEST_TIMEOUT = 20
"""Default dsf"""


@dataclass(frozen=True)
class Listing:
    """Data class for Listing."""

    make: str
    model: str
    year: int
    zipcode: int
    radius: float | None


@dataclass(frozen=True)
class SearchParams:
    """Docstring for SearchParams."""

    make: str
    model: str
    year: tuple[int, int] | int | None = None
    price: tuple[int, int] | None = None
    zipcode: int | None = None
    radius: float | None = None
