# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    aula59.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: phenriq2 <phenriq2@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/01/07 13:52:10 by phenriq2          #+#    #+#              #
#    Updated: 2024/01/07 14:28:15 by phenriq2         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# *args com args sendo um iterável (lista, tupla, set, dicionário) funciona como o * em C
lista = ["abacate", "bola", "cachorro"]
print(*lista, sep="\n")
string = "olá mundo"
print(*string, sep="\n")

# operação ternária em python é diferente de C e Java (não tem ? e :) e sim if e else na mesma linha
c = None
condicao = c is not None
print(2 if condicao else 3 if False else 4)