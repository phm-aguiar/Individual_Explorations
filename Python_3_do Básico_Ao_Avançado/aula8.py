#exercicios


nome = "Pedro"
sobrenome = "Modesto"
ano_nascimento = 1997     
maior_de_idade = (2023 - ano_nascimento) >= 18
altura_em_metros = 1.70
peso = 74
imc_acima_do_peso = peso/(altura_em_metros**2) >=25 and peso/(altura_em_metros**2) <=29.9 

print("Nome:", nome)
print("Sobrenome:", sobrenome)
print("Idade:", 2023 - ano_nascimento)
print("Maior de idade?", maior_de_idade)
print("Altura:", altura_em_metros)
print(f"Imc: {peso/(altura_em_metros**2):.2f}")
print(f"Imc acima do peso? {imc_acima_do_peso}")
