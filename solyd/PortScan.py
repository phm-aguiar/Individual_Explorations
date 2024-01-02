# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    PortScan.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: phenriq2 <phenriq2@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/01/02 17:30:23 by phenriq2          #+#    #+#              #
#    Updated: 2024/01/02 17:54:23 by phenriq2         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import socket

# Definindo o alvo
set_port = [21, 22, 23, 80, 443, 8080] # lista de portas a serem testadas
for port in set_port:
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client.settimeout(0.5)
	code = client.connect_ex(("localhost", port))
	if code == 0:
		print(port," -> OPEN")

# para verificar um servidor local, use de exemplo um servidor nc -lvp 21