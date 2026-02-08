"""Docstring for apify_api."""

import os

from apify_client import ApifyClient
from dotenv import load_dotenv
from fetchers.base_fetcher import BaseFetcher

del BaseFetcher
load_dotenv()

APIFY_KEY = os.getenv("APIFY_KEY")


def main() -> None:
    # Client initialization with the API token.
    apify_client = ApifyClient(APIFY_KEY)
    actor_client = apify_client.actor("apify/facebook-marketplace-scraper")

    run_input = {
        "startUrls": [
            {
                "url": "https://www.facebook.com/marketplace/la/gr86",
            },
            {
                "url": "https://www.facebook.com/marketplace/prague/search/?query=apartment",
            },
        ],
        "resultsLimit": 20,
    }
    call_result = actor_client.call(run_input=run_input)
    print(call_result)


if __name__ == "__main__":
    main()
