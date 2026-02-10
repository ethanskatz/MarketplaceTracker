"""Docstring for marketcheck_api."""

import os

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("MARKETCHECK_KEY")

url = "https://api.marketcheck.com/v2/search/car/active"
url = "https://api.marketcheck.com/v2/search/car/fsbo/active"

querystring = {
    "api_key": f"{API_KEY}",
    "make": "toyota",
    "model": "mr2",
}

headers = {"Accept": "application/json"}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())
