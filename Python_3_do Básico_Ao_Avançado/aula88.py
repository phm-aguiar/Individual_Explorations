# valores Truthy e Falsy
# valores mutaveis e imutaveis
# exemplos de valores mutaveis: listas, dicionarios, conjuntos
# exemplos de valores imutaveis: inteiros, floats, strings, tuplas, booleans
# lista Truthy
lista = ['a', 1, 1.1, True, 'Alberto', 'Silva', 'Prof. Alberto', 42, ['C', 'Python'], {'nome':'Alberto', 'idade':42}];
# lista Falsy
lista_falsy = [];
# dicionario Truthy
dicionario = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5};
# dicinario Falsy
dicionario_falsy = {};
# conjunto Truthy
conjunto = {1, 2, 3, 4, 5};
# conjunto Falsy
conjunto_falsy = set();
# tupla Truthy
tupla = (1, 2, 3, 4, 5);
# tupla Falsy
tupla_falsy = ();
# inteiro Truthy
inteiro = 42;
# inteiro Falsy
inteiro_falsy = 0;
# float Truthy
flutuante = 42.0;
# float Falsy
flutuante_falsy = 0.0;
# string Truthy
string = 'maicao';
# string Falsy
string_falsy = '';
# None é sempre Falsy
nada = None;
# False é sempre Falsy
falso = False;
# intervalo Truthy
intervalo = range(10);
# intervalo Falsy
intervalo_falsy = range(0);

def verifica_se_eh_truthy_ou_falsy(valor):
	if valor:
		print(f'{valor} é Truthy');
	else:
		print(f'{valor} é Falsy');
  
verifica_se_eh_truthy_ou_falsy(lista);
verifica_se_eh_truthy_ou_falsy(lista_falsy);
verifica_se_eh_truthy_ou_falsy(dicionario);
verifica_se_eh_truthy_ou_falsy(dicionario_falsy);
