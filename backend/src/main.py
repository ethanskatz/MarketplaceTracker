import os

from dotenv import load_dotenv

from src.fetchers.auto_dev_fetcher import AutoDevFetcher
from src.utils import SearchParams

if __name__ == "__main__":
    load_dotenv()

    api_key = os.getenv("AUTO_DEV_KEY")

    if api_key is None:
        raise FileNotFoundError

    fetcher = AutoDevFetcher(api_key=api_key)

    params = SearchParams(make="toyota", model="gr86", year=(2022, 2024))
    response = fetcher.get_listings(parameters=params)
    print(response)
