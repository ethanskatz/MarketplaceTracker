"""Docs."""

from dataclasses import asdict

import requests

from src.fetchers.base_fetcher import BaseFetcher
from src.utils import DEFAULT_REQUEST_TIMEOUT, Listing, SearchParams

PARAM_TO_QUERY = {
    "make": "vehicle.make",
    "model": "vehicle.model",
    "year": "vehicle.year",
    "price": "retailListing.price",
    "zipcode": "zip",
    "radius": "distance",
    "page": "page",
    "count": "limit",
}
"""Mapping of SearchParams fields to API query fields."""


class AutoDevFetcher(BaseFetcher):
    """Docstring for AutoDevFetcher."""

    def __init__(self, api_key: str) -> None:
        """Docstring for __init__.

        :param self: Description
        :param api_key: Description
        """
        super().__init__(api_key)
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

    def get_listings(self, parameters: SearchParams) -> list[Listing]:
        params = AutoDevFetcher._build_query(parameters=parameters)
        return params
        response = requests.get(
            f"https://api.auto.dev/listings?{query}",
            headers=self.headers,
            params=params,
            timeout=DEFAULT_REQUEST_TIMEOUT,
        )
        return response.text

    @staticmethod
    def _build_query(parameters: SearchParams) -> dict[str, str]:
        params = {
            key: val for key, val in asdict(parameters).items() if val is not None
        }

        if "zipcode" in params:
            params["zip"] = params.pop("zipcode")

        return params

    @staticmethod
    def _parse_response(response: str) -> list[Listing]:
        raise NotImplementedError
