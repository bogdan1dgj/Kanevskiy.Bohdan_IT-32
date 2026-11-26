import csv
import requests
import sys

print("Bohdan Kanevskiy, IT-32")

URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange"

def get_rate(code, timeout=10):
    response = requests.get(
        URL,
        params={"valcode": code, "json": ""},
        timeout=timeout
    )
    response.raise_for_status()
    data = response.json()
    return data[0]["rate"], data[0]["exchangedate"]

try:
    total = 0

    with open("data/expenses.csv", "r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            total += float(row["amount"])

    usd_rate, rate_date = get_rate("USD")
    eur_rate, eur_date = get_rate("EUR")

    print("rate date:", rate_date)
    print(f"total: {total:.2f} UAH")
    print(f"USD: {total / usd_rate:.2f}")
    print(f"EUR: {total / eur_rate:.2f}")

except requests.RequestException as error:
    print(f"Помилка запиту: {error}", file=sys.stderr)
    sys.exit(1)
except (OSError, ValueError, KeyError, IndexError) as error:
    print(f"Помилка обробки даних: {error}", file=sys.stderr)
    sys.exit(1)
