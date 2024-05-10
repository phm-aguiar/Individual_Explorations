# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    aula61.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: phenriq2 <phenriq2@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/01/07 14:34:00 by phenriq2          #+#    #+#              #
#    Updated: 2024/04/15 11:00:41 by phenriq2         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# projeto cpf
cpfv = True
while (cpfv):
	cpf = input("Digite seu CPF: ").replace(".", "").replace("-", "")
	if cpf.isnumeric() and len(cpf) == 11:
		cpfv = False
	else:
		print("CPF inválido")
indice = 0
num_1 = 0
num_2 = 0
for i in range(10, 1,-1):
	num_1 += int(cpf[indice]) * i
	num_2 += int(cpf[indice]) * (i+1)
	indice += 1
num_2 += int(cpf[indice]) * 2
num_1 = (num_1 * 10) % 11 if (num_1 * 10) % 11 <= 9 else 0
num_2 = (num_2 * 10) % 11 if (num_2 * 10) % 11 <= 9 else 0
if num_1 != int(cpf[9]) and num_2 != int(cpf[10]):
	print("cpf inválido 2")
	exit()
print(f" o cpf {cpf} é válido")
