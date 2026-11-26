import requests
import sys

print("Bohdan Kanevskiy, IT-32")

URL = "https://api.open-meteo.com/v1/forecast"

params = {
    "latitude": 50.7472,
    "longitude": 25.3254,
    "current": "temperature_2m,wind_speed_10m"
}

try:
    response = requests.get(URL, params=params, timeout=10)
    response.raise_for_status()
    data = response.json()

    current = data["current"]
    temperature = current["temperature_2m"]
    wind = current["wind_speed_10m"]

    print(f"Lutsk (50.7472, 25.3254): {temperature} C, wind {wind} km/h")

except requests.RequestException as error:
    print(f"Помилка запиту: {error}", file=sys.stderr)
    sys.exit(1)
except (KeyError, ValueError) as error:
    print(f"Помилка обробки відповіді: {error}", file=sys.stderr)
    sys.exit(1)
