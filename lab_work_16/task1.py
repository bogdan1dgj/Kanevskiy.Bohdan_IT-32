import csv
import json
import os

print("Bohdan Kanevskiyn, IT-32")

with open("data/expenses.csv", "r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)
    expenses = []

    for row in reader:
        expenses.append({
            "date": row["date"],
            "category": row["category"],
            "amount": float(row["amount"]),
            "comment": row["comment"]
        })

with open("data/expenses.json", "w", encoding="utf-8") as file:
    json.dump(expenses, file, indent=2, ensure_ascii=False)

file_size = os.path.getsize("data/expenses.json")

print(f"Кількість витрат: {len(expenses)}")
print(f"Розмір JSON-файлу: {file_size} байт")
