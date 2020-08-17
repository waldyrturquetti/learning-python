n = int(input('Digite um número:'))
aux = n

print('Calculando {}!'.format(n))
fatorial = 1

while n > 0:
	print('{}'. format(n), end=' ')
	print('x' if n > 1 else ' = ', end=' ')
	fatorial = fatorial*n
	n = n - 1


print('{}'.format(fatorial))