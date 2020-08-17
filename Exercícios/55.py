
lista = []

for c in range(0,5):
	peso = float(input('Digite o peso da pessoa {}:'.format(c+1)))
	lista.append(peso)

print(lista)

print('O maior Peso lido eh:{}'.format(max(lista)))
print('O menor Peso lido eh:{}'.format(min(lista)))
