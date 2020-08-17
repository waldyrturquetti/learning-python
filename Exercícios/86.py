matriz = [[],[],[]]

for c1 in range(3):
	for c2 in range(3):
		num = int(input(f'Digite um número para o indice [{c1},{c2}]:'))
		matriz[c1].append(num)

print()
for c1 in range(3):
	for c2 in range(3):
		print(f'[{matriz[c1][c2]:^5}]',end=' ')
	print()

