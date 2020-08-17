matriz = [[],[],[]]
somaPar = 0

for c1 in range(3):
	for c2 in range(3):
		num = int(input(f'Digite um número para o indice [{c1},{c2}]:'))
		if num % 2 == 0:
			somaPar += num
		matriz[c1].append(num)

print()
for c1 in range(3):
	for c2 in range(3):
		print(f'[{matriz[c1][c2]:^5}]',end=' ')
	print()

soma3Colun = 0
for c in range(3):
	soma3Colun = soma3Colun + matriz[c][2]

maior = max(matriz[1])
#print(maior)

print(f'Ah soma dos pares eh:{somaPar}')
print(f'Ah soma da 3 Coluna eh:{soma3Colun}')
print(f'O maior valor da segunda linha eh:{maior}')



