import json
import sys

print("Bohdan Kanevskiy, IT-32")

settings_file = "settings.json"

default_settings = {
    "owner": "Ivan Parafin",
    "group": "IT-32",
    "currency": "UAH",
    "monthly_limit": 6000,
    "categories": ["food", "transport", "fun"]
}

try:
    with open(settings_file, "r", encoding="utf-8") as file:
        settings = json.load(file)
except FileNotFoundError:
    settings = default_settings
    with open(settings_file, "w", encoding="utf-8") as file:
        json.dump(settings, file, indent=2, ensure_ascii=False)
except json.JSONDecodeError as error:
    print(f"Помилка JSON у рядку {error.lineno}", file=sys.stderr)
    sys.exit(1)

print("Налаштування:")
print(json.dumps(settings, indent=2, ensure_ascii=False))

try:
    with open("data/expenses.json", "r", encoding="utf-8") as file:
        expenses = json.load(file)
except FileNotFoundError:
    expenses = []

total = sum(expense["amount"] for expense in expenses)

print(f"Сума витрат: {total:.2f} {settings['currency']}")
print(f"Місячний ліміт: {settings['monthly_limit']} {settings['currency']}")

if total > settings["monthly_limit"]:
    print("Увага: місячний ліміт перевищено")
else:
    print("Місячний ліміт не перевищено")
