# Початкова база даних з 5 працівниками
database = [
    ["TechCorp", "Менеджер", "+380501234567", "manager@techcorp.com", 25000],
    ["SoftDev", "Розробник", "+380661234568", "dev@softdev.com", 30000],
    ["DataPro", "Аналітик", "+380731234569", "analyst@datapro.com", 28000],
    ["TechCorp", "Дизайнер", "+380501234570", "designer@techcorp.com", 22000],
    ["SoftDev", "Тестувальник", "+380661234571", "tester@softdev.com", 20000]
]

attributes = ["Назва фірми", "Посада", "Телефон", "E-мейл", "Оклад"]

print("База даних 'Працівник'")

while True:
    print("\nМеню:")
    print("a. Вивести весь список")
    print("b. Додати працівника")
    print("c. Відсортувати список за атрибутом")
    print("d. Видалити працівників за атрибутом")
    print("e. Видалити працівника за індексом")
    print("f. Вивести працівників за атрибутом")
    print("q. Вийти з програми")

    choice = input("Оберіть операцію (a-f, q): ").lower()

    if choice == 'a':
        print("\nСписок всіх працівників:")
        print("№  | Фірма      | Посада        | Телефон      | E-мейл               | Оклад")
        for i, worker in enumerate(database, 1):
            print(f"{i:<2} | {worker[0]:<10} | {worker[1]:<13} | {worker[2]:<12} | {worker[3]:<20} | {worker[4]}")

    elif choice == 'b':
        print("\nДодавання нового працівника:")
        new_worker = [
            input("Назва фірми: "),
            input("Посада: "),
            input("Телефон: "),
            input("E-мейл: "),
            int(input("Оклад: "))
        ]
        database.append(new_worker)
        print("Працівника додано до бази даних!")

    elif choice == 'c':
        print("\nДоступні атрибути для сортування:")
        for i, attribute in enumerate(attributes, 1):
            print(f"{i}. {attribute}")

        try:
            attribute_index = int(input("Введіть номер атрибута для сортування: ")) - 1
            if 0 <= attribute_index < len(attributes):
                database.sort(key=lambda x: x[attribute_index])
                print("Список відсортовано!")
            else:
                print("Невірний номер атрибута!")
        except ValueError:
            print("Будь ласка, введіть коректний номер!")

    elif choice == 'd':
        print("\nДоступні атрибути для видалення:")
        for i, attribute in enumerate(attributes, 1):
            print(f"{i}. {attribute}")

        try:
            attribute_index = int(input("Введіть номер атрибута: ")) - 1
            if 0 <= attribute_index < len(attributes):
                value = input(f"Введіть значення {attributes[attribute_index]} для видалення: ")

                deleted_count = 0
                i = 0
                while i < len(database):
                    if str(database[i][attribute_index]) == value:
                        database.pop(i)
                        deleted_count += 1
                    else:
                        i += 1

                print(f"Видалено {deleted_count} працівників!")
            else:
                print("Невірний номер атрибута!")
        except ValueError:
            print("Будь ласка, введіть коректний номер!")

    elif choice == 'e':
        try:
            index = int(input("Введіть індекс працівника для видалення: ")) - 1
            if 0 <= index < len(database):
                deleted_worker = database.pop(index)
                print(f"Працівника {deleted_worker[1]} з фірми {deleted_worker[0]} видалено!")
            else:
                print("Невірний індекс!")
        except ValueError:
            print("Будь ласка, введіть коректний індекс!")

    elif choice == 'f':
        print("\nДоступні атрибути для пошуку:")
        for i, attribute in enumerate(attributes, 1):
            print(f"{i}. {attribute}")

        try:
            attribute_index = int(input("Введіть номер атрибута: ")) - 1
            if 0 <= attribute_index < len(attributes):
                value = input(f"Введіть значення {attributes[attribute_index]}: ")

                found_workers = []
                for worker in database:
                    if str(worker[attribute_index]) == value:
                        found_workers.append(worker)

                if found_workers:
                    print(f"\nЗнайдено {len(found_workers)} працівників:")
                    print("Фірма      | Посада        | Телефон      | E-мейл               | Оклад")
                    print("-" * 70)
                    for worker in found_workers:
                        print(f"{worker[0]:<10} | {worker[1]:<13} | {worker[2]:<12} | {worker[3]:<20} | {worker[4]}")
                else:
                    print("Працівників з таким значенням не знайдено!")
            else:
                print("Невірний номер атрибута!")
        except ValueError:
            print("Будь ласка, введіть коректний номер!")

    elif choice == 'q':
        print("До побачення!")
        break

    else:
        print("Невірний вибір! Спробуйте ще раз.")