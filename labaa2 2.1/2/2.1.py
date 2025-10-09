# 1. Таблиця істинності
print("1. Таблиця істинності для x1, x2, x3 (F = x1 == x2)")
print("x1 x2 x3 | F")
for x1 in [0, 1]:
    for x2 in [0, 1]:
        for x3 in [0, 1]:
            print(f"{x1}  {x2}  {x3}  | {int(x1 == x2)}")




