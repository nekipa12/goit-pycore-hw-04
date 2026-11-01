def parse_input(user_input: str) -> tuple:
    """Розбиває введений рядок на команду та список аргументів."""
    parts = user_input.split()
    if not parts:
        return "", []
    command = parts[0].lower()
    args = parts[1:]
    return command, args


def add_contact(args: list, contacts: dict) -> str:
    """Додає новий контакт: add [ім'я] [телефон]."""
    if len(args) != 2:
        return "Give me name and phone please."
    name, phone = args
    # щоб 'john' і 'John' були одним контактом
    name = name.capitalize()
    if name in contacts:
        return "Contact already exists. Use 'change' to update it."
    contacts[name] = phone
    return "Contact added."


def change_contact(args: list, contacts: dict) -> str:
    """Змінює номер телефону існуючого контакту: change [ім'я] [телефон]."""
    if len(args) != 2:
        return "Give me name and phone please."
    name, phone = args
    name = name.capitalize()
    if name not in contacts:
        return "Contact not found."
    contacts[name] = phone
    return "Contact updated."


def show_phone(args: list, contacts: dict) -> str:
    """Показує номер телефону за ім'ям: phone [ім'я]."""
    if len(args) != 1:
        return "Give me a name please."
    name = args[0].capitalize()
    if name not in contacts:
        return "Contact not found."
    return contacts[name]


def show_all(contacts: dict) -> str:
    """Повертає всі збережені контакти."""
    if not contacts:
        return "No contacts saved yet."
    lines = []
    for name, phone in contacts.items():
        lines.append(f"{name}: {phone}")
    return "\n".join(lines)


def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        # Ctrl+C або Ctrl+D — завершуємо роботу без traceback
        print("\nGood bye!")
