valores = []

for c in range(5):
	num = int(input('Digite um valor:'))
	valores.append(num)

print(f'Você digitou {valores}')
print(f'O menor valor eh o {min(valores)}, e está no posição', end =' ')
for pos, v in enumerate(valores):
	if v == min(valores):
		print(f'{pos}...',end=' ')
print('')

print(f'O maior valor eh o {max(valores)}, e está na posição', end =' ')
for pos, v in enumerate(valores):
	if v == max(valores):
		print(f'{pos}...',end=' ')
print('')