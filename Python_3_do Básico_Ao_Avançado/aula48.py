# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    aula48.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: phenriq2 <phenriq2@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/12/24 10:39:52 by phenriq2          #+#    #+#              #
#    Updated: 2023/12/24 11:27:05 by phenriq2         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# lista = list(range(10)) 
# ou 
# lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# lista_vazia = []

# push_swap

class Node:
	def __init__(self, valor):
		self.valor = valor
		self.index = 0
		self.next = None

class chainList:
	def __init__(self):
		self.first = None

	def append_node(self, valor):
		new_node = Node(valor)
		new_node.next = self.first
		self.first = new_node

def push_a(lista_a, lista_b):
	lista_a.append_node(lista_b.first.valor)
	lista_b.first = lista_b.first.next
	print("PA")
def push_b(lista_a, lista_b):
	lista_b.append_node(lista_a.first.valor)
	lista_a.first = lista_a.first.next
	print("PB")
def swap_a(lista):
	lista.first.valor, lista.first.next.valor = lista.first.next.valor, lista.first.valor
	print("SA")
def swap_b(lista):
	lista.first.valor, lista.first.next.valor = lista.first.next.valor, lista.first.valor
	print("SB")
def swap_s(lista_a, lista_b):
	lista_a.first.valor, lista_a.first.next.valor = lista_a.first.next.valor, lista_a.first.valor
	lista_b.first.valor, lista_b.first.next.valor = lista_b.first.next.valor, lista_b.first.valor
	print("SS")
def rotate_a(lista):
	lista.append_node(lista.first.valor)
	lista.first = lista.first.next
	print("RA")
def rotate_b(lista):
	lista.append_node(lista.first.valor)
	lista.first = lista.first.next
	print("RB")
def rotate_r(lista_a, lista_b):
	lista_a.append_node(lista_a.first.valor)
	lista_a.first = lista_a.first.next
	lista_b.append_node(lista_b.first.valor)
	lista_b.first = lista_b.first.next
	print("RR")
def reverse_rotate_a(lista):
	lista.append_node(lista.first.valor)
	lista.first = lista.first.next
	print("RRA")
def reverse_rotate_b(lista):
	lista.append_node(lista.first.valor)
	lista.first = lista.first.next
	print("RRB")
def reverse_rotate_r(lista_a, lista_b):
	lista_a.append_node(lista_a.first.valor)
	lista_a.first = lista_a.first.next
	lista_b.append_node(lista_b.first.valor)
	lista_b.first = lista_b.first.next
	print("RRR")

def set_index(lista, array):
	current = lista.first
	index = 0

	while current and array:
		i = 0
		while i < len(array) and current.valor != array[i]:
			i += 1

		if i < len(array) and current.valor == array[i]:
			current.index = index
			array.pop(i)  # Use pop para remover o elemento na posição i
			index += 1
		else:
			current = current.next



import sys
lista = []
lista_a = chainList()
lista_b = chainList()
i = 0
for arg in sys.argv[1:]:
	value = (int(arg))
	lista_a.append_node(value)
	lista.append(value)

for i in range(len(lista)):
    for j in range(i + 1, len(lista)):
        if lista[i] >= lista[j]:
            lista[i], lista[j] = lista[j], lista[i]
set_index(lista_a, lista)



print(lista)
