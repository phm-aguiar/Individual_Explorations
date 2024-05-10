import os
lista_de_tarefas = []
lista_de_tarefas_desfeitas = []

def adiciona_tarefa(tarefa, lista=None):
	if lista is None:
		lista = []
	lista.append(tarefa)
	return lista

# limpando o terminal 
input_usuario = None
count = 0
os.system('clear')

while(input_usuario != 'sair'):

	print("comandos:'listar', desfazer', 'refazer', 'sair'\n")
	input_usuario = input('Digite a tarefa: ')
	if(input_usuario == 'listar'):
		print("TAREFAS:\n")
		if(len(lista_de_tarefas) == 0):
			print("Nenhuma tarefa cadastrada\n")
		else:
			for tarefa in lista_de_tarefas:
				print(tarefa)
			print()
	elif(input_usuario == 'limpar'):
		os.system('clear')
	elif(input_usuario == 'desfazer'):
		if(len(lista_de_tarefas) == 0):
			print("Nenhuma tarefa cadastrada para desfazer\n")
		else:
			lista_de_tarefas_desfeitas.append(lista_de_tarefas.pop())
	elif(input_usuario == 'refazer'):
		if(len(lista_de_tarefas_desfeitas) == 0):
			print("Não existe ação a ser refeita\n")
		else:
			lista_de_tarefas.append(lista_de_tarefas_desfeitas.pop())
	elif(input_usuario == 'sair'):
		print("Saindo...\n")
	else:
		lista_de_tarefas = adiciona_tarefa(input_usuario, lista_de_tarefas)
		print("Tarefa adicionada\n")