n1 = int(input('Digite o Primeiro valor:')) 
n2 = int(input('Digite o Segundo valor:')) 
n3 = int(input('Digite o Terceiro valor:')) 
n4 = int(input('Digite o Quatro valor:'))

tupla = (n1, n2, n3, n4)

print(f'O valor 9 apareceu {tupla.count(9)} vezes') 
if 3 in tupla:
	print(f'O primeiro 3 está na {tupla.count(3) + 1} posição') 
else:
	print('O valor 3 não aparece em nenhuma posição')

flag = False
for c in tupla:
	#print(c)
	if c % 2 == 0:
		flag = True
		break

if flag is True:
	print('Os valores pares são:',end=' ')
	for c in tupla:
		if c % 2 == 0:
			print(f'{c} ',end=' ')
	print('')
else:
	print('Essa tupla não possui números pares')






