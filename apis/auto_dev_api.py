"""curl -H "Authorization: Bearer YOUR_API_KEY" \
  https://api.auto.dev/vin/WP0AF2A99KS165242
"""

import os

import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("AUTO_DEV_KEY")
headers = {"Authorization": api_key}

make = "toyota"
model = "gr86"

response = requests.get(
    f"https://api.auto.dev/listings?vehicle.make={make}&vehicle.model={model}",
    headers=headers,
)


print(response.text)
