# try, except, else, finally

a = 42;
b = 0;

try:
	print("antes da divisão");
	b = b[0];
	print(a/b);
	print("depois da divisão");
except ZeroDivisionError:
	print('Não é possível dividir por zero');
except NameError:
	print('Variável não declarada');
except (TypeError, IndexError) as error:
	print('Tipo de variável errada');
	print(error);
	print('NOME:' , error.__class__.__name__);
except Exception:
	print('Erro genérico');

# finally: # sempre executa independente do erro ou acerto exemplo: fechar conexão com banco de dados
# fechar arquivo
# exemplo de uso: abrir arquivo, ler arquivo, fechar arquivo
try:
    arquivo = open('mamba.py', 'r')
    print(arquivo.read());
except FileNotFoundError:
	print('Arquivo não encontrado')
finally:
	arquivo.close();
    
