# try except

numero = input("Vou dobrar o número que voce digitar: ")

try:
    numero_float = float(numero)
    print(f'O dobro de {numero} é {numero_float * 2:.2f}')
except:
    print(f'"{numero}": isso nao é um numero')





