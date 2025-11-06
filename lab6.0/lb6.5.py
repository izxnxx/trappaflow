
database = [
    {"фірма": "TechCorp", "посада": "менеджер", "телефон": "0991112233", "емейл": "ivanov@techcorp.com",
     "оклад": 15000},
    {"фірма": "SoftDev", "посада": "розробник", "телефон": "0674445566", "емейл": "petrov@softdev.com", "оклад": 20000},
    {"фірма": "BizSolutions", "посада": "аналітик", "телефон": "0637778899", "емейл": "sydorenko@biz.com",
     "оклад": 18000},
    {"фірма": "TechCorp", "посада": "тестувальник", "телефон": "0501122334", "емейл": "kovalenko@techcorp.com",
     "оклад": 12000},
    {"фірма": "DataSystems", "посада": "менеджер", "телефон": "0956677889", "емейл": "shevchenko@data.com",
     "оклад": 17000}
]

while True:
    print("\nМеню:")
    print("a - Вивести весь список")
    print("b - Додати елемент")
    print("c - Сортувати за атрибутом")
    print("d - Видалити за атрибутом")
    print("e - Видалити за індексом")
    print("f - Пошук за атрибутом")
    print("q - Вийти")

    choice = input("Оберіть операцію: ")

    if choice == 'a':
        for i, item in enumerate(database):
            print(f"{i}: {item}")

    elif choice == 'b':
        new_item = {
            "фірма": input("Фірма: "),
            "посада": input("Посада: "),
            "телефон": input("Телефон: "),
            "емейл": input("Емейл: "),
            "оклад": int(input("Оклад: "))
        }
        database.append(new_item)
        print("Запис додано!")

    elif choice == 'c':
        attr = input("Атрибут для сортування: ")
        database.sort(key=lambda x: x.get(attr, ""))
        print("Відсортовано!")

    elif choice == 'd':
        attr = input("Атрибут: ")
        value = input("Значення: ")
        database = [item for item in database if item.get(attr) != value]
        print("Видалено!")

    elif choice == 'e':
        index = int(input("Індекс: "))
        if 0 <= index < len(database):
            database.pop(index)
            print("Видалено!")
        else:
            print("Невірний індекс!")

    elif choice == 'f':
        attr = input("Атрибут: ")
        value = input("Значення: ")
        for item in database:
            if item.get(attr) == value:
                print(item)

    elif choice == 'quit':
        break
