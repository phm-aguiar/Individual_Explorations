# raise - Lança uma exceção

# ex

def nao_aceito_zero(y):
	if y == 0:
		raise ZeroDivisionError('Divisão por zero')
	return True

def int_or_float(x, y):
	if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
		raise TypeError('x e y precisam ser do tipo int ou float')
	return True

def dividi(x, y) -> float:
	int_or_float(x, y)
	nao_aceito_zero(y)
	return x / y