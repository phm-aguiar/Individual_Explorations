# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    aula43.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: phenriq2 <phenriq2@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/12/18 09:51:30 by phenriq2          #+#    #+#              #
#    Updated: 2024/04/15 11:00:10 by phenriq2         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# como o for funciona em python? 
# range(start, stop, step) logo, range(0, 10, 1) é igual a range(10) e range(10, 0, -1) é igual a range(10, -1, -1)
#  a sintaxe do for é for <var> in <iterable>:
# a saidar do range para o for é um objeto do tipo range, que é um iteravel, ou seja, é um objeto que pode ser iterado


texto = "ola mundo"

for letra in texto:
	print("*"+letra, end='* ')

print("\n")

# ordem crescente
for n in range(10):
	print(n, end=' ')

print("\n")

# ordem decrescente
for n in range(10, 0, -1):
	print(n, end=' ')

print("\n")

# numeros pares de 0 a 10

for n in range(0, 11, 2):
	print(n, end=' ')

print("\n")

# iteravel -> string, lista, range, tupla, dicionario e etc
# iterador -> objeto que pode ser iterado, que retorna um valor por vez quando a função next() é chamada
# iteravel -> objeto que retorna um iterador quando a função iter() é chamada 
# iter() -> retorna um iterador == __iter__()
# next() -> retorna o proximo valor do iterador
# StopIteration -> exceção lançada quando o iterador não tem mais valores para retornar
# iterador -> __next__(), __iter__() -> retorna o proprio objeto


# implementando um for

texto = iter("ola mundo") # iter() retorna um iterador e "ola mundo" é um iteravel

while True:
	try:
		letra = next(texto)
		print(letra, end=' ')
	except StopIteration:
		break


print("\n")

for i in range(10):
	print(i, end=' ')
else:
	print("\nfor também tem else... que é executado quando o for termina sem ser interrompido por um break")
