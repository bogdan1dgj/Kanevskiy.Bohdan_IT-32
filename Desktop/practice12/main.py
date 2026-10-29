from pathlib import Path
import kanevskyi_files as files


directory = Path(__file__).parent

print("Список файлів:")
print(files.list_files(directory))

print("\nФайли з підрядком 'main':")
print(files.find_files(directory, "main"))

text = "Ім'я: Bohdan\nПрізвище: Kanevskyi\nГрупа: IT-32"

path = directory / "student_info.txt"
files.create_file(path, text)

print("\nСтворено файл:", path.name)
