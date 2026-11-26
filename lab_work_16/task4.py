import json
from datetime import date

print("Bohdan Kanevskiy, IT-32")

today = date.today()
data = {"created": today}

try:
    json.dumps(data)
except TypeError as error:
    print("Помилка стандартної серіалізації:", error)

def date_to_string(value):
    if isinstance(value, date):
        return value.isoformat()
    raise TypeError("Непідтримуваний тип")

json_text = json.dumps(data, default=date_to_string)
print("Спосіб 1:", json_text)

data_for_json = {"created": today.isoformat()}
json_text = json.dumps(data_for_json)
loaded_data = json.loads(json_text)
loaded_data["created"] = date.fromisoformat(loaded_data["created"])

print("Спосіб 2:", loaded_data)
print("Початкове і відновлене значення однакові:",
      loaded_data["created"] == today)
print("Тип відновленого значення:", type(loaded_data["created"]))
