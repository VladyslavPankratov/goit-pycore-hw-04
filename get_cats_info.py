def create_test_cats_file(path):
    data = """60b90c1c13067a15887e1ae1,Tayson,3
60b90c2413067a15887e1ae2,Vika,1
60b90c2e13067a15887e1ae3,Barsik,2
60b90c3b13067a15887e1ae4,Simon,12
60b90c4613067a15887e1ae5,Tessi,5"""
    with open(path, 'w', encoding='utf-8') as file:
        file.write(data)

def get_cats_info(path):
    cats_list = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if line:
                    parts = line.split(',')
                    if len(parts) == 3:
                        cat_id, name, age = parts
                        cat_info = {
                            "id": cat_id,
                            "name": name,
                            "age": age
                        }
                        cats_list.append(cat_info)
                    else:
                        print(f"Попередження: некоректний рядок - {line}")
    except FileNotFoundError:
        print(f"Помилка: файл за шляхом '{path}' не знайдено.")
    except Exception as e:
        print(f"Сталася помилка при читанні файлу: {e}")
    return cats_list

# --- Виконання ---
file_path = "cats_file.txt"

create_test_cats_file(file_path)              # Створюємо тестовий файл
cats_info = get_cats_info(file_path)          # Зчитуємо дані
print(cats_info)                              # Виводимо результат
