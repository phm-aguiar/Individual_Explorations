from os import system

lista_de_compras = []
system('clear')

while(1):
	try:
		print("selecione uma opção:")
		option = input("[C]adastrar, [L]istar, [R]emover, [S]air: ").lower()
		if(option == "c"):
			system('clear')
			item = input("digite o nome do item: ").capitalize()
			lista_de_compras.append(item)

		elif(option == "l"):
			system('clear')
			if (not lista_de_compras):
				print("A lista esta vazia")
			for indice, item in enumerate(lista_de_compras):
				print(f"{indice} {item}")
		elif(option == "r"):
			system('clear')
			index = int(input("indice: "))
			print(f"o item {lista_de_compras.pop(index)} foi removido")
		elif(option == "s"):
			break
		else:
			print("digite uma opção valida")
	except ValueError:
		print("digite apenas numeros")
	except IndexError:
		if len(lista_de_compras) == 0:
			system('clear')
			print("a lista está vazia... impossivel remover algo")
		else:
			system('clear')
			print(f"a lista so vai até o index {len(lista_de_compras) - 1}")
