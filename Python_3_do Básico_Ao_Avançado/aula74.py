# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    aula74.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: phenriq2 <phenriq2@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/01/12 15:08:29 by phenriq2          #+#    #+#              #
#    Updated: 2024/01/12 15:31:10 by phenriq2         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# closures e funções que retornam outras funções
# closures sao usadas quando queremos que uma 
# função lembre de seu escopo léxico


def criar_saudacao(saudacao: str) -> str:
	def saudar(nome: str) -> str:
		return f'{saudacao}, {nome.capitalize()}!'
	return saudar

bom_dia = criar_saudacao('Bom dia')
boa_tarde = criar_saudacao('Boa tarde')
boa_noite = criar_saudacao('Boa noite')

print(bom_dia(input('Digite seu nome: ')))