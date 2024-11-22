class AgeError(Exception):
    """Виняток для некоректного віку."""
    pass

class InvalidAgeTypeError(AgeError):
    """Виняток для некоректного типу віку."""
    pass

class NegativeAgeError(AgeError):
    """Виняток для від'ємного віку."""
    pass


class Student:
    def __init__(self, name, surname, grade, institution="", age=None):
        self.name = name
        self.surname = surname
        self.grade = grade
        self.institution = institution
        self.age = self._validate_age(age)


    def _validate_age(self, age):
        if age is None:
            return None # Дозволяємо None, якщо вік не задано
        if not isinstance(age, int):
            raise InvalidAgeTypeError("Вік повинен бути цілим числом.")
        if age <= 0:
            raise NegativeAgeError("Вік повинен бути більшим за нуль.")
        return age

    # ... решта коду класу Student ...


# Приклади використання:

try:
    student1 = Student("Іван", "Петров", 10, age=20)
    print(f"Студент {student1.name} {student1.surname}, вік: {student1.age}")
except AgeError as e:
    print(f"Помилка при створенні студента: {e}")

try:
    student2 = Student("Марія", "Іванова", 8, age=-5)
    print(f"Студент {student2.name} {student2.surname}, вік: {student2.age}")
except AgeError as e:
    print(f"Помилка при створенні студента: {e}")

try:
    student3 = Student("Петро", "Сидоров", 12, age="двадцять")
    print(f"Студент {student3.name} {student3.surname}, вік: {student3.age}")
except AgeError as e:
    print(f"Помилка при створенні студента: {e}")

try:
    student4 = Student("Олена", "Коваль", 7) # Вік не вказано - це допустимо
    print(f"Студент {student4.name} {student4.surname}, вік: {student4.age}")
except AgeError as e:
    print(f"Помилка при створенні студента: {e}")