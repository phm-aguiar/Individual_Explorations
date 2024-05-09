
from itertools import combinations
from itertools import permutations
from itertools import product
from itertools import groupby

pessoas = ['João', 'Maria', 'José', 'Pedro', 'Ana', 'Carlos', 'Paula', 'Márcia', 'Mário', 'Luís']

camisetas = ['P', 'M', 'G', 'GG']

print(*list(combinations(pessoas, 10)))

print(*list(permutations(camisetas, 4)))

print(*list(product(pessoas, camisetas)))

print()
alunos = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
grupos = groupby(sorted(alunos))

for key, group in grupos:
	print(key, list(group))