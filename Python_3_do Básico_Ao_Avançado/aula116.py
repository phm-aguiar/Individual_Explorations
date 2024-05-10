# trabalhando com arquivos


# Abrindo um arquivo/ criando um arquivo se ele não existir

arquivo = open('aula116.txt', 'w')

# Escrevendo no arquivo

arquivo.write('Olá, mundo!\n')

# Fechando o arquivo

arquivo.close()

# uma maneira mais simples de abrir um arquivo sem a necessidade de fechá-lo

with open('aula116.txt', 'w') as arquivo:
    # sobrescreve o arquivo
    arquivo.write('Olá, mundo bão!\n')
    # truncando o arquivo
    # o numero passado como argumento é a quantidade de bytes a serem mantidos no arquivo
    arquivo.truncate(18)
    # escrevendo no arquivo
    arquivo.write('Olá, mundo bão2!\n')
    print("arquivo.closed")

with open('aula116.txt', 'r') as arquivo:
	# lendo o arquivo
	print(arquivo.read())
 
with open('aula116.txt', 'a') as arquivo:
    arquivo.write('Olá, mundo bão3!\n')
    arquivo.write('Olá, mundo bão4!\n')

with open('aula116.txt', 'r') as arquivo:
    print(arquivo.read())

import os

os.unlink('aula116.txt')


# arquivos json

pessoa = {
	'nome': 'João',
	'sobrenome': 'Silva',
	'idade': 29,
	'estado': 'SP',
	'endereços': [
		{
			'rua': 'Rua 1',
			'numero': 123
		},
		{
			'rua': 'Rua 2',
			'numero': 456
		}
	],
	'altura': 1.75,
	'numeros favoritos': [1, 2, 3, 4, 5],
	'dev': True,
}

import json

with open('pessoa.json', 'w') as arquivo:
    json.dump(pessoa, arquivo, ensure_ascii=False, indent=4)

with open('pessoa.json', 'r') as arquivo:
	pessoa2 = json.load(arquivo)
	print(pessoa2)
	print(pessoa2['nome'])
os.unlink('pessoa.json')