# None = Null
# is None = é nulo
# is not None = não é nulo
# is é um operador de comparação que retorna True ou False se o objeto é ou não é o mesmo objeto

condicao = True
passou_no_teste = None

if condicao:
	passou_no_teste = True
	print('Passou no teste')
else:
	passou_no_teste = False
	print('Não passou no teste')

print(passou_no_teste, type(passou_no_teste))
print(passou_no_teste is None)
print(passou_no_teste is not None)
