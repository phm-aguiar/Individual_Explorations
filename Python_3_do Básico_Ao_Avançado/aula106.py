lista_1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
lista_2 = ['ba', 'sp', 'mg', 'rj']

lista_unida = zip(lista_1, lista_2)

print(list(lista_unida))

l1 = [1, 2, 3, 4, 5]
l2 = [10, 20, 30, 40, 50, 60]

soma = zip(l1, l2)

list_soma = []

for i in soma:
	somatorio = 0
	for j in i:
		somatorio += j
	list_soma.append(somatorio)
 
soma = [x + y for x, y in zip(l1, l2)]
 
print(list_soma)
print(soma)