# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    dns.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: phenriq2 <phenriq2@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/01/02 17:59:54 by phenriq2          #+#    #+#              #
#    Updated: 2024/01/02 18:02:34 by phenriq2         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import dns.resolv

dns_resolver = dns.resolver.Resolver()

resultado = dns_resolver.resolver("bancocn.com", "A")

print(resultado) # retorna um objeto do tipo dns.resolver.Answer