import csv
from pathlib import Path
from datetime import date, timedelta
import sys

print("Bohdan Kanevskiy, IT-32")

try:
    file_path = Path("data") / "expenses.csv"

    if not file_path.exists():
        raise FileNotFoundError("Файл expenses.csv не знайдено")

    today = date.today()
    week_ago = today - timedelta(days=7)

    total = 0
    expenses_count = 0

    with file_path.open("r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            expense_date = date.fromisoformat(row["date"])
            amount = float(row["amount"])

            if week_ago <= expense_date <= today:
                total += amount
                expenses_count += 1

    print(f"Кількість витрат за тиждень: {expenses_count}")
    print(f"Загальна сума витрат: {total:.2f} грн")

except Exception as error:
    print(f"Помилка: {error}", file=sys.stderr)
    sys.exit(1)