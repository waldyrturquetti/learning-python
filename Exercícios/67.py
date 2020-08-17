
print('Programa da Tabuada')

while True:
	n = int(input('Digite um valor (Digite um número negativo para sair):'))
	if n < 0:
		print('O programa encerrado')
		break
	for c in range(0,11):
		print('-'*20)
		print(f'{n} x {c} = {n*c}')
