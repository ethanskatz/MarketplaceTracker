"""Docs"""

from typing import Any

import requests
from fetchers.base_fetcher import BaseFetcher


class AutoDevFetcher(BaseFetcher):
    """Docstring for AutoDevFetcher."""

    def __init__(self, api_key: str) -> None:
        """Docstring for __init__.

        :param self: Description
        :param api_key: Description
        """
        super().__init__(api_key)
        self.headers = {"Authorization": self.api_key}

    def get_listings(
        self,
        *,
        make: str,
        model: str,
        year: tuple[int, int] | int | None = None,
    ) -> str:
        """Docstring for get_listings.

        :param self: Description
        :param make: Description
        :param model: Description
        :param year: Description
        :return: Description
        """
        kwargs: dict[str, Any] = locals().pop("self", None)
        query = AutoDevFetcher._build_query(kwargs)
        response = requests.get(
            f"https://api.auto.dev/listings?{query}",
            headers=self.headers,
            timeout=20,
        )
        return response.text

    @staticmethod
    def _build_query(kwargs: dict) -> str:
        query_arr: list[str] = []
        for key, val in kwargs.items():
            if val:
                query_arr.append(f"vehicle.{key}={val}")
        query = "&".join(query_arr)

        return query

    @staticmethod
    def _parse_response(response: str) -> str:

        return "Hello World!"


if __name__ == "__main__":
    fetcher = AutoDevFetcher(api_key=api_key)

    print(fetcher.get_listings(make="toyota", model="gr86"))
