from pathlib import Path


def get_cats_info(path: str) -> list:
    """Читає файл з даними про котів і повертає список словників."""
    cats = []

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                cat_id, name, age = line.split(",")
                # вік залишаємо рядком, як у прикладі з завдання
                cats.append({"id": cat_id, "name": name, "age": age})
    except FileNotFoundError:
        print(f"Файл {path} не знайдено.")
        return []
    except OSError as error:
        print(f"Не вдалося прочитати файл {path}: {error}")
        return []
    except ValueError:
        print(f"Файл {path} має неправильний формат даних.")
        return []

    return cats


if __name__ == "__main__":
    file_path = Path(__file__).parent / "cats_file.txt"

    cats_info = get_cats_info(str(file_path))
    for cat in cats_info:
        print(cat)

    # перевірка обробки помилки, якщо файлу не існує
    print(get_cats_info("missing_file.txt"))
