def num_average():
    count = int(input("Введіть кількість чисел: "))
    numbers = []
    for i in range(count):
        number = float(input(f"Введіть число {i + 1}: "))
        numbers.append(number)
    average = sum(numbers) / len(numbers)
    print(f"\nВведені числа: {numbers}")
    print(f"Середнє значення: {average}")

    return average
num_average()