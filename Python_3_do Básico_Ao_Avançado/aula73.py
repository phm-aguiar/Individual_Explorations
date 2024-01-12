# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    aula73.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: phenriq2 <phenriq2@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/01/12 14:43:57 by phenriq2          #+#    #+#              #
#    Updated: 2024/01/12 14:53:14 by phenriq2         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# higher order functions (funções de alta ordem)
# são funções que retornam outras funções
# ou que recebem outras funções como parâmetro

def somar(*args: list) -> int:
	result = 0
	for arg in args:
		result += arg
	return result

def subtrair(*args: list) -> int:
	result = 0
	for arg in args:
		result -= arg
	return result

def multiplicar(*args: list) -> int:
	result = 1
	for arg in args:
		result *= arg
	return result
def dividir(*args: list) -> int:
	result = 1
	for arg in args:
		result /= arg
	return result

def calcular(operacao: str, *args: list) -> int:
	if operacao == '+':
		return somar(*args)
	elif operacao == '-':
		return subtrair(*args)
	elif operacao == '*':
		return multiplicar(*args)
	elif operacao == '/':
		return dividir(*args)
	else:
		return 'Operação inválida'
	
print(calcular('-', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
