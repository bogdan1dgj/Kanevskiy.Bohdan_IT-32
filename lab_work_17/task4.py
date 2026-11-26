import requests
import sys

print("Bohdan Kanevskiy, IT-32")

mode = "connection"
if len(sys.argv) > 1:
    mode = sys.argv[1]

try:
    if mode == "connection":
        url = "https://this-domain-does-not-exist.invalid"
        timeout = 10
    elif mode == "http":
        url = "https://bank.gov.ua/this-page-does-not-exist"
        timeout = 10
    elif mode == "timeout":
        url = "https://httpbin.org/delay/3"
        timeout = 0.001
    else:
        print("Використання: python task4.py connection|http|timeout",
              file=sys.stderr)
        sys.exit(1)

    response = requests.get(url, timeout=timeout)
    response.raise_for_status()
    print("Запит виконано успішно")

except requests.ConnectionError as error:
    print(f"Помилка з'єднання: {error}", file=sys.stderr)
    sys.exit(1)
except requests.Timeout as error:
    print(f"Час очікування вичерпано: {error}", file=sys.stderr)
    sys.exit(1)
except requests.HTTPError as error:
    print(f"HTTP-помилка: {error}", file=sys.stderr)
    sys.exit(1)
except requests.RequestException as error:
    print(f"Помилка запиту: {error}", file=sys.stderr)
    sys.exit(1)
