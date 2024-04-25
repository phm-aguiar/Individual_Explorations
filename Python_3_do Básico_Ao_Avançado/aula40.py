# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    aula40.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: phenriq2 <phenriq2@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/12/17 14:52:11 by phenriq2          #+#    #+#              #
#    Updated: 2024/04/15 10:59:53 by phenriq2         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

try:
	while True:
		numero = int(input("digite um numero: "))
		numero2 = int(input("digite um numero: "))
		operador = input("digite um operador(ou qualquer outra coisa para sair): ")
		if (operador == "+"):
			print(f"resultaddo é: {numero + numero2}")
		elif (operador == "-"):
			print(f"resultaddo é: {numero - numero2}")
		elif (operador == "*"):
			print(f"resultaddo é: {numero * numero2}")
		elif (operador == "/"):
			print(f"resultaddo é: {numero / numero2}")	
		elif (operador == "//"):
			print(f"resultaddo é: {numero // numero2}")
		elif (operador == "%"):
			print(f"resultaddo é: {numero % numero2}")
		else:
			break

except:
	print("algo foi digitado com erro!!")
