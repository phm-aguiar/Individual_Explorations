def multi(*args: list) -> int:
	result = 1
	for arg in args:
		result *= arg
	return result

def par_impar(nbr: int) -> str:
	if nbr % 2 == 0:
		return 'par'
	else:
		return 'impar'

print(multi(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

print(par_impar(3))
