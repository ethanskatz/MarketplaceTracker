"""Docstring for apify_api."""

from apify_client import ApifyClient

from src.fetchers.base_fetcher import BaseFetcher


def main() -> None:
    # Client initialization with the API token.
    apify_client = ApifyClient(APIFY_KEY)
    actor_client = apify_client.actor("apify/facebook-marketplace-scraper")

    run_input = {
        "startUrls": [
            {
                "url": "https://www.facebook.com/marketplace/la/?query=gr86",
            },
            {
                "url": "https://www.facebook.com/marketplace/la/search/?query=mr2",
            },
        ],
        "resultsLimit": 20,
    }
    call_result = actor_client.call(run_input=run_input)
    print(call_result)


if __name__ == "__main__":
    main()


class ApifyFetcher(BaseFetcher):
    def __init__(self, api_key: str) -> None:
        super().__init__(api_key)
