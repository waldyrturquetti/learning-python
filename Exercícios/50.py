
lista = []

for n in range(0,6):
	num = int(input('Digite o número {}:'.format(n)))
	if num % 2 == 0:
		lista.append(num)

print('A soma dos números pares eh:{}'.format(sum(lista)))