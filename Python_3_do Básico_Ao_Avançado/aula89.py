# dir, hasattr, getattr

string = "42";

# no debug, digite dir(string) para ver os métodos disponíveis para a string
# o hasattr verifica se o objeto tem o atributo

if hasattr(string, 'split'):
	print(string.split());
# o getattr pega o atributo do objeto
	print(getattr(string, 'split')());

