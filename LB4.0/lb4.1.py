n = 3663
a = 17446
b = 93547

print("a. Квадрати чисел менші за n:")
i = 1
while True:
    square = i * i
    if square < n:
        print(square, end=" ")
        i += 1
    else:
        break
print("\n")

print("b. Цілі числа кратні 100 та менші за n:")
for num in range(100, n, 100):
    print(num, end=" ")
print("\n")

print("c. Степені двійки менші за n:")
power = 1
while power < n:
    print(power, end=" ")
    power *= 2
print("\n")

print("d. Сума всіх парних чисел між a та b:")
sum_even = 0
for num in range(a, b + 1):
    if num % 2 == 0:
        sum_even += num
print(sum_even)
print()

print("e. Сума всіх непарних чисел кратних 3 між a та b:")
sum_odd_multiple_3 = 0
for num in range(a, b + 1):
    if num % 2 != 0 and num % 3 == 0:
        sum_odd_multiple_3 += num
print(sum_odd_multiple_3)
print()

print("f. Сума всіх непарних цифр числа n:")
sum_odd_digits = 0
for digit in str(n):
    if int(digit) % 2 != 0:
        sum_odd_digits += int(digit)
print(sum_odd_digits)