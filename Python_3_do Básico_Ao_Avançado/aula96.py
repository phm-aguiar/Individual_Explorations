# import, from, as e *

# importando o modulo inteiro
import sys
# importando apenas a função exit do modulo sys
from sys import exit
# importando todas as funções do modulo sys
from sys import *
# importando apenas a função exit do modulo sys e renomeando para sair
from sys import exit as sair
print(sys.platform)

# modularização em python

from aula96_m import sum as soma

print(soma(2, '3 '))