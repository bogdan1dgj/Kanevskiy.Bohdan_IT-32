
from pathlib import Path
from tempfile import TemporaryDirectory


def list_files(directory):
    """Повертає список файлів у вказаній директорії.

    Args:
        directory: Шлях до директорії.

    Returns:
        Список назв файлів.
    """
    path = Path(directory)
    return [file.name for file in path.iterdir() if file.is_file()]


def find_files(directory, substring):
    """Шукає файли за підрядком у назві.

    Args:
        directory: Шлях до директорії.
        substring: Текст для пошуку в назві файлу.

    Returns:
        Список назв знайдених файлів.
    """
    path = Path(directory)
    return [
        file.name for file in path.iterdir()
        if file.is_file() and substring in file.name
    ]


def create_file(path, text):
    """Створює файл і записує в нього текст.

    Args:
        path: Шлях до файлу.
        text: Текст для запису.

    Returns:
        Шлях до створеного файлу.
    """
    file = Path(path)
    file.write_text(text, encoding="utf-8")
    return str(file)


if __name__ == "__main__":
    with TemporaryDirectory() as directory:
        create_file(Path(directory) / "test.txt", "Тест")
        create_file(Path(directory) / "main.py", "print('Hello')")

        print("Усі файли:", list_files(directory))
        print("Пошук main:", find_files(directory, "main"))
        print("Самоперевірку завершено.")
