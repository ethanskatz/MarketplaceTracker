class BaseAggregator:

    def __init__(self, api_key: str) -> None:
        """Docstring for __init__

        :param self: Description
        :param api_key: Description
        :type api_key: str
        """
        self.api_key = api_key

    def get_listings(self):
        pass
