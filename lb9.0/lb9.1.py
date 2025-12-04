class Employee:
    def __init__(self, company, position, phone, email, salary):
        self.__company = company
        self.__position = position
        self.__phone = phone
        self.__email = email
        self.__salary = salary

    def get_company(self): return self.__company
    def get_position(self): return self.__position
    def get_phone(self): return self.__phone
    def get_email(self): return self.__email
    def get_salary(self): return self.__salary

    def set_company(self, val): self.__company = val
    def set_position(self, val): self.__position = val
    def set_phone(self, val): self.__phone = val
    def set_email(self, val): self.__email = val
    def set_salary(self, val): self.__salary = val


    def __eq__(self, other): return self.__salary == other.__salary
    def __lt__(self, other): return self.__salary < other.__salary
    def __le__(self, other): return self.__salary <= other.__salary
    def __gt__(self, other): return self.__salary > other.__salary
    def __ge__(self, other): return self.__salary >= other.__salary
    def __str__(self):
        return f"{self.__company} | {self.__position} | {self.__phone} | {self.__email} | ${self.__salary}"

class EmployeeDB:
    def __init__(self):
        self.__employees = []
        self.__index = 0

    def __len__(self):
        return len(self.__employees)

    def __iter__(self):
        return self

    def __next__(self):
        if self.__index < len(self.__employees):
            result = self.__employees[self.__index]
            self.__index += 1
            return result
        self.__index = 0
        raise StopIteration

    def add(self, emp):
        self.__employees.append(emp)

    def print_all(self):
        for emp in self.__employees:
            print(emp)

    def sort_by(self, attr):
        key_map = {
            'company': lambda e: e.get_company(),
            'position': lambda e: e.get_position(),
            'phone': lambda e: e.get_phone(),
            'email': lambda e: e.get_email(),
            'salary': lambda e: e.get_salary()
        }
        if attr in key_map:
            self.__employees.sort(key=key_map[attr])

    def remove_by_attribute(self, attr, value):
        remove_methods = {
            'company': lambda e: e.get_company() == value,
            'position': lambda e: e.get_position() == value,
            'phone': lambda e: e.get_phone() == value,
            'email': lambda e: e.get_email() == value,
            'salary': lambda e: e.get_salary() == value
        }
        self.__employees = [e for e in self.__employees if not remove_methods[attr](e)]

    def remove_by_index(self, index):
        if 0 <= index < len(self.__employees):
            del self.__employees[index]

    def filter_by_attribute(self, attr, value):
        filter_methods = {
            'company': lambda e: e.get_company() == value,
            'position': lambda e: e.get_position() == value,
            'phone': lambda e: e.get_phone() == value,
            'email': lambda e: e.get_email() == value,
            'salary': lambda e: e.get_salary() == value
        }
        return [str(e) for e in self.__employees if filter_methods[attr](e)]


def main():
    db = EmployeeDB()
    db.add(Employee("Google", "Developer", "+380991234567", "dev@google.com", 5000))
    db.add(Employee("Microsoft", "Manager", "+380992345678", "manager@microsoft.com", 4500))
    db.add(Employee("Apple", "Designer", "+380993456789", "designer@apple.com", 5500))

    while True:
        print("\n1. Вивести всіх")
        print("2. Додати працівника")
        print("3. Сортувати за атрибутом")
        print("4. Видалити за атрибутом")
        print("5. Видалити за індексом")
        print("6. Фільтрувати за атрибутом")
        print("0. Вихід")

        choice = input("Виберіть опцію: ")

        if choice == "1":
            db.print_all()

        elif choice == "2":
            company = input("Фірма: ")
            position = input("Посада: ")
            phone = input("Телефон: ")
            email = input("Email: ")
            salary = int(input("Оклад: "))
            db.add(Employee(company, position, phone, email, salary))

        elif choice == "3":
            attr = input("Атрибут для сортування (company/position/phone/email/salary): ")
            db.sort_by(attr)
            print("Відсортовано!")

        elif choice == "4":
            attr = input("Атрибут (company/position/phone/email/salary): ")
            value = input("Значення для видалення: ")
            if attr == 'salary':
                value = int(value)
            db.remove_by_attribute(attr, value)
            print("Видалено!")
            
        elif choice == "5":
            index = int(input("Індекс для видалення: "))
            db.remove_by_index(index)
            print("Видалено!")

        elif choice == "6":
            attr = input("Атрибут для фільтрації (company/position/phone/email/salary): ")
            value = input("Значення: ")
            if attr == 'salary':
                value = int(value)
            results = db.filter_by_attribute(attr, value)
            for r in results:
                print(r)

        elif choice == "0":
            break


if __name__ == "__main__":
    main()