n1 = int(input('Digite o número 1:'))
n2 = int(input('Digite o número 2:'))
n3 = int(input('Digite o número 3:'))

#Verificando quem é o maior
if n1 >= n2 and n1 >= n3:
	print('n1 é o maior número')
elif n2 >= n1 and n2 >= n3:
	print('n2 é o maior número')
else:
 	print('n3 é o maior número')

#Verificando quem é o menor
if n1 <= n2 and n1 <= n3:
	print('n1 é o menor número')
elif n2 <= n1 and n2 <= n3:
	print('n2 é o menor número')
else:
 	print('n3 é o menor número')


