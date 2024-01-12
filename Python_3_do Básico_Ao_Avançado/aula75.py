# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    aula75.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: phenriq2 <phenriq2@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/01/12 15:54:51 by phenriq2          #+#    #+#              #
#    Updated: 2024/01/12 15:59:30 by phenriq2         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def calcular(nbr: int) -> str:
		def mult(operation: int) -> int:
			return nbr * operation
		return mult
try:
	nbr = int(input('Digite um número: '))
	operacao = int(input('Digite a operação (2 - duplicar, 3 - triplicar, 4 - quadruplicar,...): '))
	print(calcular(nbr)(operacao))
except:
	print('Error on input')