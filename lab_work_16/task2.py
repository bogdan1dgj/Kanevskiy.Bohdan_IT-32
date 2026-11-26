import json
from datetime import date

print("Bohdan Kanevskiy, IT-32")

with open("data/expenses.json", "r", encoding="utf-8") as file:
    expenses = json.load(file)

new_expense = {
    "date": date.today().isoformat(),
    "category": "food",
    "amount": 150.0,
    "comment": "lunch"
}
expenses.append(new_expense)

before = len(expenses)
expenses = [expense for expense in expenses if expense["amount"] >= 10]
deleted_count = before - len(expenses)

with open("data/expenses_updated.json", "w", encoding="utf-8") as file:
    json.dump(expenses, file, indent=2, ensure_ascii=False)

print("Додано витрат: 1")
print(f"Видалено витрат менше 10: {deleted_count}")
print(f"Залишилося витрат: {len(expenses)}")
