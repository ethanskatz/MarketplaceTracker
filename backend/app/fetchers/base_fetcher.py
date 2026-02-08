"""Docstring for apis.base_api."""

from abc import ABC, abstractmethod

from app.utils import Listing


class BaseFetcher(ABC):
    """Base Class for content fetchers."""

    def __init__(self, api_key: str) -> None:
        """Docstring for __init__.

        :param self: Description
        :param api_key: Description
        :type api_key: str
        """
        self.api_key = api_key

    @abstractmethod
    def get_listings(self, query, count: int | None = None) -> list[Listing]:
        """Docstring for get_listings.

        :param self: Description
        :return: Description
        :rtype: list[Listing]
        """

    @abstractmethod
    def _build_query(**kwargs) -> str:
        """Docstring for build_query.

        :param kwargs: Description
        :return: Query containing xyz.
        :rtype: str
        """
