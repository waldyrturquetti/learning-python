numeros = [[],[]]
#print(numeros)

for c in range(7):
	num = int(input('Digite um número:'))
	if num % 2 == 0:
		numeros[0].append(num)
	else:
		numeros[1].append(num)

#print(numeros)

print(f'A lista dos pares digitados:{numeros[0]}')
print(f'A lista dos ímpares digitados:{numeros[1]}')
