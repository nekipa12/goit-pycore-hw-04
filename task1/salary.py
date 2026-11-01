from pathlib import Path


def total_salary(path: str) -> tuple:
    """Повертає загальну та середню зарплату розробників з файлу."""
    salaries = []

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                # порожні рядки просто пропускаємо
                if not line:
                    continue
                name, salary = line.split(",")
                salaries.append(float(salary))
    except FileNotFoundError:
        print(f"Файл {path} не знайдено.")
        return 0, 0
    except OSError as error:
        print(f"Не вдалося прочитати файл {path}: {error}")
        return 0, 0
    except ValueError:
        print(f"Файл {path} має неправильний формат даних.")
        return 0, 0

    # якщо у файлі немає жодного запису, ділити на нуль не можна
    if not salaries:
        print(f"Файл {path} порожній.")
        return 0, 0

    total = sum(salaries)
    average = round(total / len(salaries), 2)
    return total, average


if __name__ == "__main__":
    # файл з даними лежить поруч зі скриптом
    file_path = Path(__file__).parent / "salary_file.txt"

    total, average = total_salary(str(file_path))
    print(
        f"Загальна сума заробітної плати: {total}, "
        f"Середня заробітна плата: {average}"
    )

    # перевірка обробки помилки, якщо файлу не існує
    total, average = total_salary("missing_file.txt")
    print(
        f"Загальна сума заробітної плати: {total}, "
        f"Середня заробітна плата: {average}"
    )
