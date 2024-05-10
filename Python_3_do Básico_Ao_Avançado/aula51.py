# empacotamento e desempacotamento de listas

lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

# a, b, c, d, e, f, g, h = lista
#  cada variável recebe um elemento da lista

a, b, *c = lista
# a recebe o primeiro elemento, b recebe o segundo elemento e c recebe o restante dos elementos da lista

a, *b, c = lista
# a recebe o primeiro elemento, b recebe o restante dos elementos e c recebe o último elemento da lista

a,*_ = lista
# a recebe o primeiro elemento e o resto é descartado 

_, b, *_ = lista
print(b, _)

