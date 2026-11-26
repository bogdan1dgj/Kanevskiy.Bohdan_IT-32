import json
import os
import sys
from datetime import datetime
import requests

print("Bohdan Kanevskiy, IT-32")

URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange"
CACHE_FILE = "cache/rates.json"

try:
    rates = None
    source = ""

    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "r", encoding="utf-8") as file:
            cache = json.load(file)

        saved_time = datetime.fromisoformat(cache["saved_at"])
        age = (datetime.now() - saved_time).total_seconds()

        if age < 3600:
            rates = cache["rates"]
            source = f"cache (age {int(age)} s)"

    if rates is None:
        response = requests.get(URL, params={"json": ""}, timeout=10)
        response.raise_for_status()
        rates = response.json()

        os.makedirs("cache", exist_ok=True)
        cache = {
            "saved_at": datetime.now().isoformat(),
            "rates": rates
        }

        with open(CACHE_FILE, "w", encoding="utf-8") as file:
            json.dump(cache, file, indent=2, ensure_ascii=False)

        source = "api (cache saved)"

    print("source:", source)
    print("currencies:", len(rates))

except requests.RequestException as error:
    print(f"Помилка запиту: {error}", file=sys.stderr)
    sys.exit(1)
except (OSError, ValueError, KeyError, TypeError) as error:
    print(f"Помилка кешу або даних: {error}", file=sys.stderr)
    sys.exit(1)
