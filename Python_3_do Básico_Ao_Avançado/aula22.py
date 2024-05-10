def verificação(a, b, c):
    return ((a == 'E' or a == 'e') and (b == c))


entrada = input('[E]ntrar [S]air: ')
senha_digitada = str(input('Senha: '))

senha_permitida = '123456'
l = [entrada, senha_digitada, senha_permitida]

if verificação(*l):
    print('Entrar')
else:
    print('Sair')

