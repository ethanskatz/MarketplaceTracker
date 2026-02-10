"""Docstring for apis.base_api."""

from abc import ABC, abstractmethod

from src.utils import Listing, SearchParams


class BaseFetcher(ABC):
    """Base Class for content fetchers."""

    def __init__(self, api_key: str) -> None:
        """Create instance of .

        :param self: Description
        :param api_key: Description
        :type api_key: str
        """
        self.api_key = api_key

    @abstractmethod
    def get_listings(self, parameters: SearchParams) -> list[Listing]:
        """Get listings matching specified parameters.

        :param self: Description
        :return: Description
        :rtype: list[Listing]
        """
        ...

    @staticmethod
    @abstractmethod
    def _build_query(parameters: SearchParams) -> dict[str, str]:
        """Docstring for build_query.

        :param kwargs: Description
        :return: Query containing xyz.
        :rtype: str
        """
        ...

    @staticmethod
    @abstractmethod
    def _parse_response(response: str) -> list[Listing]:
        """Docstring for _parse_response.

        :param response: Description
        :type response: str
        :return: Description
        :rtype: list[Listing]
        """
        ...
