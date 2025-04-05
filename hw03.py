import sys
from pathlib import Path
from colorama import init, Fore, Style

# Ініціалізація colorama
init(autoreset=True)

def print_directory_tree(path: Path, prefix: str = ""):
    try:
        entries = sorted(path.iterdir(), key=lambda x: (x.is_file(), x.name.lower()))
        for index, entry in enumerate(entries):
            connector = "┗━ " if index == len(entries) - 1 else "┣━ "
            if entry.is_dir():
                print(f"{prefix}{connector}{Fore.BLUE}{entry.name}{Style.RESET_ALL}")
                new_prefix = prefix + ("   " if index == len(entries) - 1 else "┃  ")
                print_directory_tree(entry, new_prefix)
            else:
                print(f"{prefix}{connector}{Fore.GREEN}{entry.name}{Style.RESET_ALL}")
    except PermissionError:
        print(f"{prefix}{Fore.RED}Permission denied: {path}{Style.RESET_ALL}")

def main():
    if len(sys.argv) != 2:
        print(f"{Fore.RED}Помилка: Вкажіть шлях до директорії як аргумент командного рядка.{Style.RESET_ALL}")
        print("Приклад: python hw03.py /шлях/до/директорії")
        sys.exit(1)

    input_path = Path(sys.argv[1])

    if not input_path.exists():
        print(f"{Fore.RED}Помилка: Вказаний шлях не існує.{Style.RESET_ALL}")
        sys.exit(1)
    if not input_path.is_dir():
        print(f"{Fore.RED}Помилка: Вказаний шлях не є директорією.{Style.RESET_ALL}")
        sys.exit(1)

    print(f"{Fore.CYAN}Структура директорії: {input_path}{Style.RESET_ALL}")
    print_directory_tree(input_path)

if __name__ == "__main__":
    main()
