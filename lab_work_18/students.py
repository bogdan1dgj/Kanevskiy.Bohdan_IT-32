class Student:
    """Студент зі списком оцінок за 12-бальною шкалою."""

    college = "ФКТБП ВНУ"

    def __init__(self, name, surname, group):
        self.name = name
        self.surname = surname
        self.group = group
        self.grades = []

    def full_name(self):
        return f"{self.name} {self.surname}"

    def add_grade(self, grade):
        if not 1 <= grade <= 12:
            raise ValueError(f"Оцінка має бути від 1 до 12, отримано {grade}")
        self.grades.append(grade)

    def average(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0.0

    def card(self):
        return f"{self.full_name():<16} {self.group:<6} середній бал {self.average():.2f}"


class Group:
    """Група студентів."""

    def __init__(self, code):
        self.code = code
        self.students = []

    def add(self, student):
        self.students.append(student)

    def best(self):
        return max(self.students, key=lambda s: s.average())

    def report(self):
        lines = [f"Група {self.code}, студентів: {len(self.students)}"]

        for student in sorted(self.students, key=lambda s: s.average(), reverse=True):
            lines.append("  " + student.card())

        return "\\n".join(lines)


if __name__ == "__main__":
    group = Group("IT-32")

    for name, surname, grades in [
        ("Богдан", "Каневський", [10, 12, 11]),
        ("Тарас", "Мельник", [7, 8, 9]),
        ("Ірина", "Шевчук", [12, 11, 12])
    ]:
        student = Student(name, surname, group.code)

        for grade in grades:
            student.add_grade(grade)

        group.add(student)

    print(group.report())
    print("Найкращий студент:", group.best().full_name())
