def is_acceptable_password(password: str) -> bool:
	return len(password) > 6

# len(password) > 6 retorna True se o tamanho da senha for maior que 6
# password: str indica que o argumento password é uma string
# -> bool indica que a função retorna um valor booleano
# esta é uma forma de definir os tipos de argumentos e o tipo de retorno da função em Python
# não é obrigatório, mas é uma boa prática de programação

# argumentos nomeados

def args_nomeados(nome, sobrenome):
	print(f"Olá {nome} {sobrenome}")
	print(f"{nome=} {sobrenome=}")

args_nomeados("João", "Silva")
args_nomeados(nome="Silva", sobrenome="João")
args_nomeados(sobrenome="Silva", nome="João")
# args_nomeados(nome="João", "Silva") # erro de sintaxe
# args_nomeados("João", sobrenome="Silva") # erro de sintaxe
# args nomeados devem vir depois dos argumentos posicionais e servem para evitar erros de sintaxe

# definir um valor padrão para um argumento

def args_padrao(nome, sobrenome="Silva", idade = None):
	if idade is not None:
		print(f"Olá {nome} {sobrenome} sua idade é {idade}")
	else:
		print(f"Olá {nome} {sobrenome}")

args_padrao("João", "macedo")

# manipulação de variáveis globais
x = 1
def print_x():
	x = 0
	print(x)
	def print_x2():
		x = 2
		print(x)
	print_x2()
print_x()
print(x)

def print_x_global():
	global x
	x = 0
	print(x)
	def print_x2():
		x = 2
		print(x)
	print_x2()
print_x_global()
print(x)