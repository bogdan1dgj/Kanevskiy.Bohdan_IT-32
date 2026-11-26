from math import ceil
from pathlib import Path
import sys

print("Bohdan Kanevskiy, IT-32")

try:
    length = 5.5
    width = 4.2
    height = 2.7

    tile_length = 0.3
    tile_width = 0.3
    tile_price = 45

    floor_area = length * width
    room_volume = length * width * height
    perimeter = 2 * (length + width)

    tile_area = tile_length * tile_width
    tiles_count = ceil(floor_area / tile_area)
    total_price = tiles_count * tile_price

    print(f"Площа кімнати: {floor_area:.2f} м2")
    print(f"Об'єм кімнати: {room_volume:.2f} м3")
    print(f"Периметр кімнати: {perimeter:.2f} м")
    print(f"Кількість плиток: {tiles_count}")
    print(f"Вартість плитки: {total_price} грн")

except Exception as error:
    print(f"Помилка: {error}", file=sys.stderr)
    sys.exit(1)