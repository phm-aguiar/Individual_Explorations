# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    portscan.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: phenriq2 <phenriq2@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/01/02 17:22:12 by phenriq2          #+#    #+#              #
#    Updated: 2024/01/02 17:29:43 by phenriq2         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import socket

# Definindo o alvo
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# conectando ao alvo na porta 80, connect recebe uma tupla com o alvo e a porta
client.connect(('bancocn.com', 80))
# enviando dados ao alvo, send recebe uma string em bytes
client.send(b"hello world")

# recebendo dados do alvo, recv recebe a quantidade de bytes a serem recebidos
# e retorna uma string em bytes
resposta = client.recv(4096)
# decodificando a string em bytes para string normal, decode serve para transformar bytes em string
print(resposta.decode())