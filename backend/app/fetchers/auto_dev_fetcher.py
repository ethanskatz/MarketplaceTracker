import os

import requests
from dotenv import load_dotenv

from backend.app.fetchers.base_fetcher import BaseFetcher
from backend.app.utils import Listing

load_dotenv()

api_key = os.getenv("AUTO_DEV_KEY")


class AutoDevFetcher(BaseFetcher):
    """Docstring for AutoDevFetcher."""

    def __init__(self, api_key: str) -> None:
        super().__init__(api_key)
        self.headers = {"Authorization": self.api_key}

    def get_listings(self, query, count: int | None = None) -> list[Listing]:
        query = self._build_query()

        make = "toyota"
        model = "gr86"
        response = requests.get(
            f"https://api.auto.dev/listings?vehicle.make={make}&vehicle.model={model}",
            headers=self.headers,
            timeout=20,
        )
        return response.text

    def _build_query(**kwargs) -> str:
        return super()._build_query()


if __name__ == "__main__":
    fetcher = AutoDevFetcher(api_key=api_key)
