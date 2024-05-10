def generator():
	for i in range(5):
		yield i
	return 'Fim da função'

# g = generator()
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g)) # StopIteration: Fim da função

# recapiulando yield  é um return que não mata a função, ele pausa a função e retorna o valor

def generator():
	for i in range(5):
		yield i
	return 'Fim da função'

def generator2():
	yield from generator()
	yield 'Agora sim acabou'
	return 'Fim da função'

g = generator2()

for i in g:
	print(i) # 0, 1, 2, 3, 4, 'Agora sim acabou'
 
#  yield from delega a execução para outro generator