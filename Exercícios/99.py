def maior(num):
	if num != []:
		maior = max(num)
		print(f'A lista = {num}, possui {len(num)} valores')
		print(f'O maior valor eh:{maior}')
	else:
		print('Não existe valor maior, a lista possui 0 valores')

def maior2(*num):

	if num != ():
		maior = max(num)
		print(f'A lista = {num}, possui {len(num)} valores')
		print(f'O maior valor eh:{maior}')
	else:
		print('Não existe valor maior, a lista possui 0 valores')

valores = []

while True:

	while True:
		op = str(input('Deseja Inserir um número na lista [S/N]?')).strip().upper()[0]
		if op == 'N'or op == 'S':
			break
	if op == 'N':
		break

	numero = int(input('Digite um valor:'))
	valores.append(numero)

#print(valores)
maior(valores)
print('=-'*20)

maior2(2,5,67,9,100)
maior2(4,6,7,8,9,0,2,1,100,200)
maior2()


