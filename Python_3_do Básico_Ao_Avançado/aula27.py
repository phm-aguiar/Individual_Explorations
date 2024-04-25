"""
fatiamento [i:f:p] inicio fim passo


len retorna a quantidade de caracteres


"""

counter = 0
variavel = 'olá mundo'
print(len(variavel[2: -1:2]))
print(len(variavel))
print(variavel[::-1])

while counter < len(variavel):
    print(variavel[counter], end='')
    counter += 1

