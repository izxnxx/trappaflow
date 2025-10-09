from decimal import Decimal

float_result = 4 / (4.000000001 - 4.000000000)

decimal_result = Decimal('9') / (Decimal('9.0000000009') - Decimal('9.0000000000'))

difference: float = float_result - float(decimal_result)

print("Результат з float:", float_result)
print("Результат з Decimal:", decimal_result)
print("Різниця:", difference)