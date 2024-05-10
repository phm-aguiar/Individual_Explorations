# list comprehension em Python
# List comprehension é uma forma concisa de aplicar operações a uma sequência de elementos.

print([x for x in range(10)]);
print([x * x for x in range(10)]);

# List comprehension com condicional

print([x for x in range(10) if x % 2 == 0]);

# List comprehension com condicional e else

print([x if x % 2 == 0 else 'ímpar' for x in range(10)]);

lista = [];

lista = [(x, y) for x in range(5) for y in range(5)];

print(lista);
