def sum(a: int,b: int) -> int:
	return a + b

if(__name__ == '__main__'):
	print(sum(2, 3))
	try:
		print(sum(2, '3'))
	except TypeError as e:
		print(f'Erro: {e}')