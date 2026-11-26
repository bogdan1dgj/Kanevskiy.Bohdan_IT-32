import requests
import sys

print("Bohdan Kanevskiy, IT-32")

URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange"

try:
    response = requests.get(URL, params={"json": ""}, timeout=10)
    response.raise_for_status()
    rates = response.json()

    print("status:", response.status_code)
    print("Content-Type:", response.headers.get("Content-Type"))
    print("currencies:", len(rates))

    for item in rates:
        if item["cc"] == "USD" or item["cc"] == "EUR":
            print(item["cc"], item["rate"], item["exchangedate"])

except requests.RequestException as error:
    print(f"Помилка запиту: {error}", file=sys.stderr)
    sys.exit(1)
