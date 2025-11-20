from typing import List, Dict, Any

database: List[Dict[str, Any]] = [
    {"фірма": "TechCorp", "посада": "Розробник", "телефон": "380501234567", "емейл": "dev@techcorp.com", "оклад": 25000},
    {"фірма": "FinanceLLC", "посада": "Бухгалтер", "телефон": "380631234568", "емейл": "account@financellc.com", "оклад": 18000},
    {"фірма": "TechCorp", "посада": "Менеджер", "телефон": "380671234569", "емейл": "manager@techcorp.com", "оклад": 30000},
    {"фірма": "MarketPro", "посада": "Маркетолог", "телефон": "380501234570", "емейл": "marketing@marketpro.com", "оклад": 22000},
    {"фірма": "FinanceLLC", "посада": "Аналітик", "телефон": "380631234571", "емейл": "analyst@financellc.com", "оклад": 28000},
]
def print_all(db: List[Dict[str, Any]]) -> None:
    for idx, item in enumerate(db, 1):
        print(f"{idx}. {item['фірма']} - {item['посада']} - {item['оклад']} грн")

def add_item(db: List[Dict[str, Any]]) -> None:
    item = {
        "фірма": input("Фірма: "),
        "посада": input("Посада: "),
        "телефон": input("Телефон: "),
        "емейл": input("Емейл: "),
        "оклад": int(input("Оклад: "))
    }
    db.append(item)
    print("Додано!")

def sort_by_attribute(db: List[Dict[str, Any]], attr: str) -> None:
    db.sort(key=lambda x: x.get(attr, ""))
def delete_by_attribute(db: List[Dict[str, Any]], attr: str, value: Any) -> None:
    db[:] = [item for item in db if item.get(attr) != value]
def delete_by_index(db: List[Dict[str, Any]], index: int) -> None:
    if 0 <= index < len(db):
        db.pop(index)
        print("Видалено!")
    else:
        print("Невірний індекс")

def filter_by_attribute(db: List[Dict[str, Any]], attr: str, value: Any) -> List[Dict[str, Any]]:
    return [item for item in db if item.get(attr) == value]

def main() -> None:
    while True:
        print("\nМеню:")
        print("a - Вивести всіх")
        print("b - Додати")
        print("c - Сортувати")
        print("d - Видалити за атрибутом")
        print("e - Видалити за індексом")
        print("f - Пошук")
        print("q - Вийти")
        choice = input("Ваш вибір: ").lower()
        if choice == "a":
            print_all(database)
        elif choice == "b":
            add_item(database)
        elif choice == "c":
            attr = input("Атрибут для сортування: ")
            sort_by_attribute(database, attr)
        elif choice == "d":
            attr = input("Атрибут: ")
            value = input("Значення: ")
            if attr == "оклад":
                value = int(value)
            delete_by_attribute(database, attr, value)
        elif choice == "e":
            index = int(input("Індекс: ")) - 1
            delete_by_index(database, index)
        elif choice == "f":
            attr = input("Атрибут: ")
            value = input("Значення: ")
            if attr == "оклад":
                value = int(value)
            result = filter_by_attribute(database, attr, value)
            print_all(result)
        elif choice == "q":
            break
        else:
            print("Невірний вибір")

if __name__ == "__main__":
    main()