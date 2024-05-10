#empacotamento e desenpacotamento de argumentos

# empacotamento simples

""" a,b = 1,2;
a,b = b,a;
print(a,b);

pessoa = {'nome':'Prof. Alberto', 'idade':42, 'cursos':['C', 'Python']};

a, b, c = pessoa;

print(a);
print(b);
print(c);

a, b, c = pessoa.values();

print(a);
print(b);
print(c);

a, b, c = pessoa.items();

print(a);
print(b);
print(c);

(a, b), (c, d), (e, f) = pessoa.items();

print(a);
print(b);
print(c);
print(d);
print(e);
print(f);


pessoa_completa = {**pessoa, **resto_da_pessoa};

print(pessoa_completa); """

resto_da_pessoa = {'sobrenome':'Silva', 'estado':'SP'};
def mostro_argumentos_nomeados(**kwargs):
	print(kwargs);

mostro_argumentos_nomeados(nome='Alberto', idade=42);
mostro_argumentos_nomeados(**resto_da_pessoa);

