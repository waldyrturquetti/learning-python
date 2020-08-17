tupla = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Transferidor', 4.20)

print('-'*40)
print(f'{"LISTAGEM DOS PREÇOS":^40}')
print('-'*40)

for c in range(0, len(tupla), 2):
	print(f'{tupla[c]:.<20}R$ {tupla[c + 1]:2}') 
print('-'*40)

'''
for pos in range(0, len(tupla)):
	if pos % 2 == 0:
		print(f'{tupla[pos]:.<30}',end='')
	else:
		print(f'R${tupla[pos]:>5.2f}')

'''