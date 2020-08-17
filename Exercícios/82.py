numeros = []
pares = []
impares = []

while True:
	num =  int(input('Digite um valor:'))
	numeros.append(num)
	op = str(input('Deseja continuar [S/N]:')).upper().strip()[0]
	if op == 'N':
		break

for n in numeros:
	if n % 2 == 0:
		pares.append(n)
	else:
		impares.append(n)

print(f'A lista Original:{numeros}')
print(f'A lista de Pares:{pares}')
print(f'A lista de impares:{impares}') 

