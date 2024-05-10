# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    aula62.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: phenriq2 <phenriq2@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/01/07 18:50:53 by phenriq2          #+#    #+#              #
#    Updated: 2024/04/15 11:00:46 by phenriq2         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from random import randint
valido = False
while(not valido):
	cpf = str(randint(100000000, 999999999))
	indice = 0
	num_1 = 0
	num_2 = 0
	for i in range(10, 1,-1):
		num_1 += int(cpf[indice]) * i
		num_2 += int(cpf[indice]) * (i+1)
		indice += 1
	num_1 = (num_1 * 10) % 11 if (num_1 * 10) % 11 <= 9 else 0
	num_2 += int(num_1) * 2
	num_2 = (num_2 * 10) % 11 if (num_2 * 10) % 11 <= 9 else 0
	cpf = cpf + str(num_1) + str(num_2)
	if len(cpf) == 11:
		valido = True
print(cpf)