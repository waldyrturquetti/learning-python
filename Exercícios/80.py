numeros = []

for c in range(5):
	num = int(input('Digite um valor:'))
	if numeros == []:												#Poderia ser feito para simplificar se o num é maior que o último elemento,
		numeros.append(num)											#sendo assim facilitaria
		print('O valor foi adicionado na lista vazia')
	else:
		for c2 in range(0,len(numeros)):
			if numeros[c2] > num:
				numeros.insert(c2, num)
				print(f'O valor {num} foi adicionado na posição {c2}')
				break
			elif c2 == len(numeros) - 1:
				numeros.append(num)
				print(f'O valor foi adicionado no final lista, ou seja posição {c2 + 1}')
				break
						

print('=-='*20)
print(f'Os valores da lista em ordem {numeros}')

