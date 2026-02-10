import os

from dotenv import load_dotenv

from backend.app.fetchers.auto_dev_fetcher import AutoDevFetcher

if __name__ == "__main__":
    load_dotenv()

    api_key = os.getenv("AUTO_DEV_KEY")
    fetcher = AutoDevFetcher(api_key=api_key)

    fetcher.get_listings(make="toyota", model="gr86")
