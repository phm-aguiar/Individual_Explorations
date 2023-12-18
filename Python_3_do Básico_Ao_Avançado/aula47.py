# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    aula47.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: phenriq2 <phenriq2@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/12/18 11:28:55 by phenriq2          #+#    #+#              #
#    Updated: 2023/12/18 13:04:00 by phenriq2         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


frutas = ['maçã', 'banana', 'morango', 'uva', 'abacaxi', 'laranja', 'melancia' 'manga']

for indice, fruta in enumerate(frutas):
	print(f"Índice: {indice}, Fruta: {fruta}")

print("\n")

import os
palavra = "banana"
saft = "*"*len(palavra)
tentativas = 0
while True:
	resposta = input("Digite uma letra: ")
	tentativas+=1
	if len(resposta) != 1:
		print("Digite apenas uma letra.")
		continue

	if resposta in palavra:
		for i, letra in enumerate(palavra):
			if resposta == letra:
				saft = saft[:i] + letra + saft[i+1:]
				print(saft)
	else:
		print(saft)
	if saft == palavra:
		# clear e mensagem de fim de jogo
		os.system('clear')
		print("Fim de jogo!")
		print(f"Você acertou a palavra '{palavra}' com {tentativas} tentativas.")
		break
print("\n")
	


