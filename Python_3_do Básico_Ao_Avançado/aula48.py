# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    aula48.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: phenriq2 <phenriq2@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/12/24 10:39:52 by phenriq2          #+#    #+#              #
#    Updated: 2024/04/15 11:00:14 by phenriq2         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# lista = list(range(10)) 
# ou 
# lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# lista_vazia = []
#  append() adiciona um elemento no final da lista
# lista.append(10)
# insert() adiciona um elemento em uma posição específica
# lista.insert(0, -1)
# pop() remove o último elemento da lista
# lista.pop()
# remove() remove um elemento específico da lista
# lista.remove(2)
# del() remove um elemento específico da lista
# del(lista[2])
# clear() remove todos os elementos da lista
# lista.clear()
# extend() adiciona uma lista a outra
# lista.extend([10, 11, 12])

lista_a = [1, 2, 3]
lista_b = lista_a
lista_a.append(4)
print(lista_b)

# lista_b está recebendo a lista_a, então quando adicionamos um elemento a lista_a, a lista_b também recebe esse elemento pois estao apontando para o mesmo endereço de memória
# para resolver isso, podemos usar o método copy() ou fatiamento de lista

lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

for letter, index in enumerate(lista):
	print(letter, index)


