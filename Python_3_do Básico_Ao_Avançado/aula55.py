# pontos flutuantes imprecisos

import decimal

print(1.1 + 2.2)
print(decimal.Decimal(1.1) + decimal.Decimal(2.2))
print(decimal.Decimal(1.1) + decimal.Decimal(2.2) == decimal.Decimal(3.3))
print(round(1.1 + 2.2, 2))
print(round(1.1 + 2.2, 1))
print(f"{1.1 + 2.2:.1f}")

