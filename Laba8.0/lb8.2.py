import json
import os
from typing import List, Dict, Any


class Database:
    def __init__(self):
        self.data: List[Dict[str, Any]] = [
            {"фірма": "TechCorp", "посада": "менеджер", "телефон": "0991112233", "емейл": "ivanov@techcorp.com",
             "оклад": 15000},
            {"фірма": "SoftDev", "посада": "розробник", "телефон": "0674445566", "емейл": "petrov@softdev.com",
             "оклад": 20000},
            {"фірма": "BizSolutions", "посада": "аналітик", "телефон": "0637778899", "емейл": "sydorenko@biz.com",
             "оклад": 18000},
            {"фірма": "TechCorp", "посада": "тестувальник", "телефон": "0501122334", "емейл": "kovalenko@techcorp.com",
             "оклад": 12000},
            {"фірма": "DataSystems", "посада": "менеджер", "телефон": "0956677889", "емейл": "shevchenko@data.com",
             "оклад": 17000}
        ]
        self.fields = ["фірма", "посада", "телефон", "емейл", "оклад"]

    def load_from_file(self, filename: str = "database.json") -> bool:
        try:
            if os.path.exists(filename):
                with open(filename, 'r', encoding='utf-8') as f:
                    self.data = json.load(f)
                print(f"БД завантажена ({len(self.data)} записів)")
                return True
            return False
        except Exception as e:
            print(f"Помилка: {e}")
            return False

    def save_to_file(self, filename: str = "database.json") -> bool:
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(self.data, f, ensure_ascii=False, indent=2)
            print("БД збережена")
            return True
        except Exception as e:
            print(f"Помилка: {e}")
            return False

    def display_all(self):
        for i, record in enumerate(self.data, 1):
            print(f"{i}: {record}")

    def add_record(self):
        try:
            record = {}
            for field in self.fields:
                record[field] = input(f"{field}: ")
            record["оклад"] = int(record["оклад"])
            self.data.append(record)
            print("Запис додано")
        except Exception as e:
            print(f"Помилка: {e}")

    def sort_by_attribute(self):
        attr = input("Атрибут для сортування: ")
        if attr in self.fields:
            self.data.sort(key=lambda x: str(x.get(attr, "")).lower())
            print("Відсортовано")

    def delete_by_attribute(self):
        attr = input("Атрибут: ")
        value = input("Значення: ")
        self.data = [r for r in self.data if str(r.get(attr, "")).lower() != value.lower()]
        print("Видалено")

    def delete_by_index(self):
        try:
            idx = int(input("Індекс: ")) - 1
            if 0 <= idx < len(self.data):
                self.data.pop(idx)
                print("Видалено")
        except:
            print("Помилка")

    def display_by_attribute(self):
        attr = input("Атрибут: ")
        value = input("Значення: ")
        filtered = [r for r in self.data if str(r.get(attr, "")).lower() == value.lower()]
        for i, record in enumerate(filtered, 1):
            print(f"{i}: {record}")


def main():
    db = Database()
    db.load_from_file()

    while True:
        print("\nМеню:")
        print("1 - Вивести всю БД")
        print("2 - Додати запис")
        print("3 - Сортувати за атрибутом")
        print("4 - Видалити за атрибутом")
        print("5 - Видалити за індексом")
        print("6 - Пошук за атрибутом")
        print("7 - Зберегти БД")
        print("8 - Завантажити БД")
        print("0 - Вийти")

        choice = input("Оберіть дію: ")

        if choice == "1":
            db.display_all()
        elif choice == "2":
            db.add_record()
        elif choice == "3":
            db.sort_by_attribute()
        elif choice == "4":
            db.delete_by_attribute()
        elif choice == "5":
            db.delete_by_index()
        elif choice == "6":
            db.display_by_attribute()
        elif choice == "7":
            db.save_to_file()
        elif choice == "8":
            db.load_from_file()
        elif choice == "0":
            break

if __name__ == "__main__":
    main()