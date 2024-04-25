# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    aula77.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: phenriq2 <phenriq2@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/01/13 15:36:05 by phenriq2          #+#    #+#              #
#    Updated: 2024/04/15 11:01:12 by phenriq2         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# perguntas

perguntas = [
	{
		'pergunta': 'Quanto é 2 + 2?',
		'opções': {
			'a': '1',
			'b': '4',
			'c': '5',
			'd': '7'
		},
		'resposta_certa': 'b'
	},
	{
		'pergunta': 'Quanto é 3 * 2?',
		'opções': {
			'a': '4',
			'b': '10',
			'c': '6',
			'd': '7'
		},
		'resposta_certa': 'c'
	},
	{
		'pergunta': 'Quanto é 2 // 3?',
		'opções': {
			'a': '0',
			'b': '1',
			'c': '2',
			'd': '3'
		},
		'resposta_certa': 'a'
	}
]

respostas_certas = 0

for i in perguntas:
	keys = list(i.keys())
	print(f"{keys[0]}: {i[keys[0]]}")
	print()
	print(f"{keys[1].capitalize()}: ")
	for j in i[keys[1]]:
		print(f"{j.capitalize()}: {i[keys[1]][j]}")
	ok = None
	while not ok:
		resposta = input("escolha uma opção: ".capitalize())
		if resposta in i[keys[1]]:
			ok = True
		else:
			print("Opção inválida!")
	if resposta == i[keys[2]]:
		print("Você acertou!")
		respostas_certas += 1
	else:
		print("Você errou!")
print(f"Você acertou {respostas_certas} de {len(perguntas)} perguntas")
