# goit-pycore-hw-04

Домашнє завдання до тем 5–6: робота з файлами, обробка винятків, модулі та віртуальне оточення.

## Структура

- `task1/salary.py` — `total_salary(path)`: загальна та середня зарплата з файлу
- `task2/cats.py` — `get_cats_info(path)`: список словників з даними про котів
- `task3/dir_tree.py` — виведення структури директорії з підсвічуванням кольорами (colorama)
- `task4/bot.py` — консольний бот-помічник

## Запуск

```
python task1/salary.py
python task2/cats.py
python task4/bot.py
```

Для `task3` потрібне віртуальне оточення з бібліотекою colorama:

```
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python task3/dir_tree.py /шлях/до/директорії
```
