
players = {
    "Іван": 3,
    "Марія": 1,
    "Петро": 2,
    "Олена": 4,
    "Андрій": 5
}

sorted_by_name = dict(sorted(players.items(), key=lambda item: item[0]))
sorted_by_rank = dict(sorted(players.items(), key=lambda item: item[1]))

print("Гравці, відсортовані за іменем:")
for name, rank in sorted_by_name.items():
    print(f"{name}: {rank} місце")

print("\nГравці, відсортовані за призовим місцем:")
for name, rank in sorted_by_rank.items():
    print(f"{rank} місце: {name}")