# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    aula42.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: phenriq2 <phenriq2@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/12/17 15:03:47 by phenriq2          #+#    #+#              #
#    Updated: 2024/04/15 11:00:03 by phenriq2         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

frase = "qual letra mais se                         repete nesta frase"

i = 0
counter = 0
current = 0
while i < (len(frase)):
	letter = frase[i]
	counter = frase.count(letter)
	if counter	> current and letter != ' ':
		repeat = letter
		current = counter
	i += 1

print(f"a letra que mais se repete é '{repeat}' {current}")
