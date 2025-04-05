def parse_input(user_input):
    """Розбирає введену команду та її аргументи."""
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args, contacts):
    """Додає новий контакт до словника."""
    if len(args) != 2:
        return "Invalid command."
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts):
    """Змінює номер телефону існуючого контакту."""
    if len(args) != 2:
        return "Invalid command."
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Contact not found."


def show_phone(args, contacts):
    """Виводить номер телефону для зазначеного контакту."""
    if len(args) != 1:
        return "Invalid command."
    name = args[0]
    return contacts.get(name, "Contact not found.")


def show_all(contacts):
    """Виводить всі контакти та їхні номери телефонів."""
    if contacts:
        return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())
    else:
        return "No contacts found."


def main():
    """Основна функція для обробки команд користувача."""
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ").strip()
        command, *args = parse_input(user_input)

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
    main()
