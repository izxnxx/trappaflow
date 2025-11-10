def empolyee():
    name = input(f"Імя працівника: ")
    surname = input(f"Прізвище працівника: ")
    salary = input(f"Зарплата прпцівника: ")

    print(f"ПІ = {surname} {name}\nЗарплата = {salary} ")
    return name, surname, salary
empolyee()