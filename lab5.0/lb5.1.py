
formula = lambda n: n**2 + 7*n
n, elements = 4, 16

lst = [formula(n + i*4) for i in range(elements)]
print(f"Початковий: {lst}")

print(f"a: {lst[3:6]}")
lst[0] = lst[-1]
print(f"b: {lst}")
combined = lst + lst.copy()
print(f"c: {combined}")
combined.extend(combined[:3])
print(f"d: {combined}")
print(f"e: max={max(combined)}, min={min(combined)}")
avg = sum(combined)/len(combined)
filtered = [x for x in combined if x >= avg]
print(f"f: {filtered}")