"""Docstring for apis.base_api."""

from abc import ABC, abstractmethod

from utils import Listing


class BaseFetcher(ABC):
    """Docstring for BaseAggregator."""

    def __init__(self, api_key: str) -> None:
        """Docstring for __init__.

        :param self: Description
        :param api_key: Description
        :type api_key: str
        """
        self.api_key = api_key

    @abstractmethod
    def get_listings(self, query) -> list[Listing]:
        """Docstring for get_listings.

        :param self: Description
        :return: Description
        :rtype: list[Listing]
        """
        return [Listing(1)]

    def build_query():
        pass

    @abstractmethod
    def fetch_from_api(self) -> None:
        pass
