numeros = []

while True:
	num =  int(input('Digite um valor:'))
	numeros.append(num)
	op = str(input('Deseja continuar [S/N]:')).upper().strip()[0]
	if op == 'N':
		break

print('=-='*20)
print(f'A lista:{numeros}')
print(f'A quantidade:{len(numeros)}')
numeros.sort(reverse=True)
print(f'A lista decrescente:{numeros}')
if 5 in numeros:
	print('O valor 5 está na lista')
else:
	print('O valor 5 não está na lista')