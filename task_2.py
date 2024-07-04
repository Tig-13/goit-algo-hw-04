def get_cats_info(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            cats = []
            for line in file:
                cat_id, name, age = line.strip().split(',')
                cats.append({
                    "id": cat_id,
                    "name": name,
                    "age": age
                })
            return cats
    except FileNotFoundError:
        print(f"File at {path} not found.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

# Приклад використання функції
cats_info = get_cats_info("path/to/cats_file.txt")
print(cats_info)
