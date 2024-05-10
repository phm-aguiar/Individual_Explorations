lista = ['a', 1, 1.1, True, 'Alberto', 'Silva', 'Prof. Alberto', 42, ['C', 'Python'], {'nome':'Alberto', 'idade':42}];

for item in lista:
	if (isinstance(item, bool)):
		print(f'{item} é booleano');
	elif (isinstance(item, int)):
		print(f'{item} é inteiro');
	elif (isinstance(item, float)):
		print(f'{item} é float');
	elif (isinstance(item, str)):
		print(f'{item} é string');
	else:
		print(f'{item} é de outro tipo');
