# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    aula39.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: phenriq2 <phenriq2@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/12/17 14:40:01 by phenriq2          #+#    #+#              #
#    Updated: 2024/04/15 10:59:49 by phenriq2         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

string = "exercicio sobre fatiamento de strings"

i = 0
novastring = ""
while i < len(string):
	novastring += "*" + string[i] 
	i += 1
print(novastring)
