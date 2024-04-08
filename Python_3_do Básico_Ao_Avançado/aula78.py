# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    aula78.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: phenriq2 <phenriq2@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/03/13 15:47:36 by phenriq2          #+#    #+#              #
#    Updated: 2024/03/13 16:10:21 by phenriq2         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# aula sobre set
# set é uma coleção de elementos únicos
# set é uma coleção não ordenada
# set é uma coleção mutável
# set é uma coleção que não aceita elementos duplicados
# set pode ser usado para remover elementos duplicados de uma lista

s1 = set()
s1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
s1.add('phenriq2')
s1.update('42')
# update itera sobre a string e adiciona cada caractere como um elemento do set
s1.remove(1)
# remove remove um elemento do set
# add adiciona um elemento ao set
s1.discard(2)
# discard remove um elemento do set
# print(s1, type(s1))

s2 = {1,2,3}
s3 = {3,4,5}

s4 = s2 | s3
s5 = s2 & s3
s6 = s2 - s3
s7 = s2 ^ s3
print(s4, s5, s6, s7)

# o | é a união de dois sets (s2 e s3) no expemplo acima ficaria {1,2,3,4,5}
# o & é a interseção de dois sets (s2 e s3) no expemplo acima ficaria {3}
# o - é a diferença de dois sets (s2 e s3) no expemplo acima ficaria {1,2}
# o ^ é a diferença simétrica de dois sets (s2 e s3) no expemplo acima ficaria {1,2,4,5}
