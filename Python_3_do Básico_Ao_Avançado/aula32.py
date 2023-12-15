"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

try:
	numero = input("Digite um Numero inteiro: ")
	numero = int(numero)
	if(numero % 2 == 0):
		print(f"esse numero é par")
	else:
		print(f"esse Numero é impar")

except ValueError:
	print("Não é um numero inteiro")

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""


try:
	hora = input("Que horas são? ")
	hora = int(hora)
	dia = 0<= hora <= 11
	tarde = 12<= hora <= 17
	noite = 18<= hora <= 23

	if dia:
		print("bom dia")
	elif tarde:
		print("boa tarde")
	elif noite:
		print("boa noite")
	else:
		print("Digite uma hora valida")


except:
	print("Digite uma hora valida")

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
"""

name = input("digite seu primeiro nome: ")
number = len(name)
small = number<= 4
medium = 5 <= number <= 6
big = 6 < number

if(small):
	print("Seu nome é curto")
elif(medium):
	print("Seu nome é normal")
elif(big):
	print("Seu nome é muito grande")
else:
	print("Digite um nome valido")


