import sys
from pathlib import Path

from colorama import Fore, init

# autoreset повертає стандартний колір після кожного print
init(autoreset=True)

DIR_COLOR = Fore.CYAN
FILE_COLOR = Fore.GREEN


def print_tree(directory: Path, prefix: str = " ") -> None:
    """Рекурсивно виводить вміст директорії у вигляді дерева."""
    try:
        items = sorted(directory.iterdir())
    except PermissionError:
        print(f"{prefix}┗ {Fore.RED}немає доступу до директорії")
        return

    for index, item in enumerate(items):
        is_last = index == len(items) - 1
        branch = "┗ " if is_last else "┣ "

        if item.is_dir():
            print(f"{prefix}{branch}{DIR_COLOR}📂{item.name}")
            # після останнього елемента вертикальну лінію далі не малюємо
            child_prefix = prefix + ("  " if is_last else "┃ ")
            print_tree(item, child_prefix)
        else:
            print(f"{prefix}{branch}{FILE_COLOR}📜{item.name}")


def main():
    if len(sys.argv) < 2:
        print("Вкажіть шлях до директорії: python dir_tree.py <шлях>")
        sys.exit(1)

    directory = Path(sys.argv[1])

    if not directory.exists():
        print(f"Шлях '{directory}' не існує.")
        sys.exit(1)

    if not directory.is_dir():
        print(f"'{directory}' не є директорією.")
        sys.exit(1)

    print(f"{DIR_COLOR}📦{directory.resolve().name}")
    print_tree(directory)


if __name__ == "__main__":
    main()
