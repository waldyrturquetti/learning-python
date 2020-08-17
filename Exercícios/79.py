numeros = []

while True:
	num = int(input('Digite um valor:'))
	if num in numeros:
		print('Valor já está na lista, não será adicionado...')
	else:
		numeros.append(num)
	
	op = str(input('Você deseja continuar [S/N]:')).upper().strip()[0]
	if op in 'N':
		break

print('=-='*20)
numeros.sort()
print(f'Você Digiteou os valores {numeros}') 