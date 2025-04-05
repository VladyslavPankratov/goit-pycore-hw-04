# Створення тестового файлу з 20 розробниками
with open("salary_file.txt", "w", encoding="utf-8") as file:
    file.write("""Alex Korp,3000
Nikita Borisenko,2000
Sitarama Raju,1000
John Smith,3500
Jane Doe,4000
Bob Johnson,2800
Alice Brown,3200
Tom Hanks,3100
Emma Watson,2900
Chris Evans,3300
Scarlett Johansson,3400
Mark Ruffalo,2700
Natalie Portman,3600
Robert Downey,5000
Jeremy Renner,2500
Elizabeth Olsen,3900
Paul Rudd,3100
Benedict Cumberbatch,4200
Brie Larson,3700
Samuel Jackson,4600""")

# Функція для розрахунку
def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            total = 0
            count = 0
            for line in file:
                parts = line.strip().split(',')
                if len(parts) != 2:
                    continue
                try:
                    salary = float(parts[1])
                    total += salary
                    count += 1
                except ValueError:
                    continue

            if count == 0:
                return (0, 0)

            average = total / count
            return (total, average)

    except FileNotFoundError:
        print(f"Файл не знайдено: {path}")
        return (0, 0)
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return (0, 0)

# Запуск функції
total, average = total_salary("salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
