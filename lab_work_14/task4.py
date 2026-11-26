import math
import random
from datetime import date, datetime, timedelta
import sys

print("Bohdan Kanevskiy, IT-32")

try:
    birth_year = 2009

    random.seed(birth_year)

    number = random.randint(1, 100)
    angle = 45

    radians = math.radians(angle)

    print(f"Випадкове число: {number}")
    print(f"Квадрат числа: {math.sqrt(number):.2f}")
    print(f"Синус кута {angle}: {math.sin(radians):.2f}")
    print(f"Косинус кута {angle}: {math.cos(radians):.2f}")

    today = date.today()
    birthday = date(birth_year, 7, 7)

    age = today.year - birthday.year
    if today < date(today.year, 7, 7):
        age -= 1

    print(f"Дата сьогодні: {today}")
    print(f"Рік народження: {birth_year}")
    print(f"Вік: {age}")

    future_date = today + timedelta(days=30)
    print(f"Дата через 30 днів: {future_date}")

    current_time = datetime.now()
    print(f"Поточна дата і час: {current_time}")

except Exception as error:
    print(f"Помилка: {error}", file=sys.stderr)
    sys.exit(1)