n1 = int(input('Digite n1:'))
n2 = int(input('Digite n2:'))
op = 1

while op != 5: 
	print(
'''
===============================
O que deseja fazer:
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa
===============================''')
	op = int(input('Digite o número referente a opção:'))

	if op == 1:
		print('A soma desses dois números eh:{}'.format(n1+n2))

	elif op == 2:
		print('A multiplicação desses dois números eh:{}'.format(n1*n2))

	elif op == 3:
		if n1 > n2:
			print('O primeiro número é maior')
		elif n1 < n2:
			print('O segundo número é maior')
		else:
			print('Os dois números são iguais')

	elif op == 4:
		n1 = int(input('Digite n1:'))
		n2 = int(input('Digite n2:'))

	elif op == 5:
		print('Você saiu do programa')

	else:
		print('Opção Inválida')

