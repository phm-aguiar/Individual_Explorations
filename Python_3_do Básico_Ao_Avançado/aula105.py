# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    aula105.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: phenriq2 <phenriq2@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/05 14:09:09 by phenriq2          #+#    #+#              #
#    Updated: 2024/05/05 14:11:46 by phenriq2         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def decoradora(func):
    print("Executando decorador 1")
    def aninhada(*args, **kwargs):
        print("aninhada")
        res = func(*args, **kwargs)
        return res
    return aninhada

@decoradora
def soma(a, b):
	return a + b


dez_mais_vinte = soma(10, 20)
print(dez_mais_vinte)