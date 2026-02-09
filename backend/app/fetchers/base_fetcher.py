"""Docstring for apis.base_api."""

from abc import ABC, abstractmethod


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
    def get_listings(
        self,
        *,
        make: str,
        model: str,
        year: tuple[int, int] | int | None = None,
    ) -> list:
        """Get listings matching specified parameters.

        :param self: Description
        :return: Description
        :rtype: list[Listing]
        """

    @staticmethod
    @abstractmethod
    def _build_query(**queryargs: dict[str, str]) -> str:
        """Docstring for build_query.

        :param kwargs: Description
        :return: Query containing xyz.
        :rtype: str
        """

    @staticmethod
    @abstractmethod
    def _parse_response(self, response: str):
        pass
