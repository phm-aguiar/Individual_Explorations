# and se um fica falso toda a expressão fica falso
# 0 0.0 '' False
# None == não valor


def verificação(a, b, c):
    return ((a == 'E') and (b == c))


entrada = input('[E]ntrar [S]air: ')
senha_digitada = str(input('Senha: '))

senha_permitida = '123456'
l = [entrada, senha_digitada, senha_permitida]

if verificação(*l):
    print('Entrar')
else:
    print('Sair')
