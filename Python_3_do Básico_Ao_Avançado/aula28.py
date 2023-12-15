nome = input("digite seu nome: ")
idade = input("digite sua idade: ")
if nome and idade:
    print(f"Seu nome é: {nome}")
    print(f"Seu nome invertido é: {nome[::-1]}")
    print(f"Seu nome contem: {len(nome)} letras")
    print(f"Seu nome contem: {nome.count(' ')} espaços")
    print(f"A primeira letra do seu nome é: {nome[0]}")
    print(f"A ultima letra do seu nome é: {nome[-1]}")
else:
    print("Desculpe, voce deixou campos vazios")
