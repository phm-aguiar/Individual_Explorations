
def adiciona_clientes(cliente, lista=None):
	if lista is None:
		lista = []
	lista.append(cliente)
	return lista


lista1 = adiciona_clientes('João')
lista2 = adiciona_clientes('Maria')
lista3 = adiciona_clientes('José')

print(lista1)
print(lista2)
print(lista3)

adiciona_clientes('João', lista2)
adiciona_clientes('Maré', lista2)
adiciona_clientes('José', lista2)

print(lista2)