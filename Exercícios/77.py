tupla = ('Bucetaa', 'Comeer', 'Poucas', 'Isso', 'Foodasse')

for c1 in range(len(tupla)):
	palavra = tupla[c1].upper()
	#print(palavra)
	print(f'Na palavra {palavra} temos',end=' ')
	for c2 in range(len(palavra)):
		if 'A' == palavra[c2]:
			print('A',end=' ')
		if 'E' == palavra[c2]:
			print('E',end=' ')
		if 'I' == palavra[c2]:
			print('I',end=' ')
		if 'O' == palavra[c2]:
			print('O',end=' ')
		if 'U' == palavra[c2]:
			print('U',end=' ')
	print('')

'''
Poderia ser feito dessa maneira:
for palavra in tupla:
	print(f'Na palavra {palavra.upper()} temos',end=' ')
	for letra in palavra:
		if letra.upper() in 'AEIOU':
			print(letra, end=' ')
'''

