maior = lambda a,b:a>b
igual = lambda a,b: a==b
numero_1 = input("digite o primeiro valor ")
numero_2 = input("digite o segundo valor ")

if maior(numero_1,numero_2):
  print("o numero 1 é maior que o numero 2")
elif igual(numero_1,numero_2):
  print("os numeros sao iguais")
else:
  print("o numero 2 é maior que o numero 1")
