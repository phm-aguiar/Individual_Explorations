# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    aula76.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: phenriq2 <phenriq2@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/01/12 16:01:18 by phenriq2          #+#    #+#              #
#    Updated: 2024/04/15 11:08:48 by phenriq2         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# dicionarios em python
# dicionarios são estruturas de dados que armazenam
# dados em forma de chave e valor
# dicionarios são representados por {}
# chaves sao como indices, mas podem ser de qualquer tipo
# dict = {'chave': 'valor'} é um exemplo de dicionario
# com 'chave' sendo uma string e 'valor' sendo outra string
# dict = {1: 'valor'} é um exemplo de dicionario
# com 1 sendo um inteiro e 'valor' sendo uma string

pessoa = {
	'nome': 'Pedro',
	'sexo': 'M',
	'idade': 26,
	'altura': 1.70,
	'peso': 75.0,
	'aluno': True
}

# para criar um dicionario vazio podemos usar
# dict = {} ou dict = dict()
# para adicionar um elemento ao dicionario
# dict['chave'] = valor 
# para remover um elemento do dicionario
# del dict['chave']
# para alterar um elemento do dicionario
# dict['chave'] = novo_valor
# para acessar um elemento do dicionario
# dict['chave']

print("\nkeys: \n")
for k in pessoa.keys():
	print(k)
print("\nvalues: \n")
for v in pessoa.values():
	print(v)
print("\nitems: \n")	
for i in pessoa.items():
	print(i)
	
if pessoa.get('peso') != None:
	print(pessoa.get('peso'))
if pessoa.get('cpf') != None:
	print(pessoa['peso'])

# o metodo get retorna o valor da chave passada
# caso a chave nao exista, ele retorna None
# podemos passar um segundo parametro para o metodo get
# que sera retornado caso a chave nao exista
# pessoa.get('cpf', '000.000.000-00')
# como a chave cpf nao existe, o metodo get retorna
# o valor padrao passado como segundo parametro
# o setdefault adiciona um elemento padrao ao dicionario
# caso o elemento nao exista no dicionario
# se o elemento existir, ele nao faz nada
pessoa.setdefault('cpf', '000.000.000-00')

pessoa2 = pessoa.copy()
# copia o dicionario pessoa para pessoa2
# porem a copia é rasa, ou seja, se houver uma lista
# dentro do dicionario, a lista é copiada por referencia
# e nao por valor, entao se alterarmos a lista em pessoa
# a lista em pessoa2 tambem sera alterada
# para copiar por valor, temos que usar o deepcopy
from copy import deepcopy

pessoa3 = deepcopy(pessoa)
# agora a copia é profunda, entao se alterarmos a lista
# em pessoa, a lista em pessoa3 nao sera alterada

deletado = pessoa3.pop('cpf')
# o metodo pop remove um elemento do dicionario e retorna
# o valor do elemento removido
deletado = pessoa3.popitem()
# o metodo popitem remove o ultimo elemento do dicionario
# e retorna uma tupla com a chave e o valor do elemento removido
pessoa3.clear()
# o metodo clear remove todos os elementos do dicionario


pessoa.update({'cpf': '000.000.000-00'})
# o metodo update adiciona um elemento ao dicionario
# caso o elemento nao exista no dicionario
# se o elemento existir, ele altera o valor do elemento
# para o valor passado como parametro
# podemos passar varios elementos ao mesmo tempo

pessoa.update({'cpf': '999.999.999-99', 'rg': '00.000.000-0'})
# aqui o metodo update altera o valor do elemento cpf e adiciona o elemento rg

# update tambem funciona com listas de tuplas
pessoa.update([('cpf', '111.111.111-11'), ('rg', '11.111.111-1')])
# aqui o metodo update altera o valor do elemento cpf e adiciona o elemento rg


