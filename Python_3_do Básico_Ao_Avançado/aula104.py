# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    aula104.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: phenriq2 <phenriq2@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/05 13:48:20 by phenriq2          #+#    #+#              #
#    Updated: 2024/05/05 13:52:41 by phenriq2         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def criar_funcao(func):
	def interna(*args, **kwargs):
		print("Função executada com sucesso")
		for arg in args:
			e_string(arg)
		resultado = func(*args, **kwargs)
		print("Função finalizada com sucesso")
		return resultado
	return interna

@criar_funcao
def invert_string(string):
	return string[::-1]

def e_string(arg):
	if isinstance(arg, str):
		print(f"{arg} é uma string")
	else:
		print(f"{arg} não é uma string")
  
print(invert_string("Ola mundo"))
print(invert_string("42"))